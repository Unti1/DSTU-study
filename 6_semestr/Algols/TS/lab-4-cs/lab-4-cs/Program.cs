using System;
using System.Collections.Generic;
using System.Linq;

namespace lab_4_cs
{
    class Program
    {
        static ProcessItemsCalculation CalculateItems(List<List<int>> matrix)
        {
            var result = new ProcessItemsCalculation();

            result.Sums = matrix.Select(e => e.Sum()).ToArray();
            result.Min = result.Sums.Min();
            result.Max = result.Sums.Max();
            result.Delta = result.Max - result.Min;
            result.MinIndex = Array.IndexOf(result.Sums, result.Min);
            result.MaxIndex = Array.IndexOf(result.Sums, result.Max);

            return result;
        }

        static List<List<int>> ProcessItems(List<List<int>> matrix)
        {
            //var copy = new List<List<int>>(matrix);
            var copy = matrix.Select(e => new List<int>(e)).ToList();

            while (true)
            {
                var calc = CalculateItems(copy);
                var cur = Utils.GetFirstElementLowerThan(copy[calc.MaxIndex], calc.Delta);

                if (cur.HasValue)
                {
                    //var index = copy[calc.MaxIndex].IndexOf(cur.Value);
                    copy[calc.MaxIndex].Remove(cur.Value);
                    copy[calc.MinIndex].Add(cur.Value);
                }
                else
                {
                    break;
                }
            }

            while (true)
            {
                bool swapOut = false;
                ProcessItemsCalculation calc = CalculateItems(copy);

                for (var i = 0; i < copy[calc.MaxIndex].Count; i++)
                {
                    var value = copy[calc.MaxIndex][i];
                    var lowers = Utils.GetElementsLowerThan(copy[calc.MinIndex], value);

                    if (lowers.Count == 0)
                        continue;

                    bool swapIn = false;

                    for (var j = 0; j < lowers.Count; j++)
                    {
                        var cur = lowers[j];

                        //var clone = new List<List<int>>(copy);
                        var clone = copy.Select(e => new List<int>(e)).ToList();
                        var indexMin = clone[calc.MinIndex].IndexOf(cur);
                        var indexMax = clone[calc.MaxIndex].IndexOf(value);

                        if (indexMin == -1 || indexMax == -1)
                            continue;

                        clone[calc.MinIndex][indexMin] = value;
                        clone[calc.MaxIndex][indexMax] = cur;

                        var newCalc = CalculateItems(clone);

                        if (newCalc.Delta < calc.Delta)
                        {
                            swapOut = true;
                            swapIn = true;
                            copy = clone;
                            calc = CalculateItems(clone);
                        }
                    }

                    if (swapIn == true)
                    {
                        break;
                    }
                }

                if (swapOut == false)
                {
                    break;
                }
            }

            return copy;
        }

        static List<List<int>> CriticalFill(List<int> array, int count)
        {
            var processors = new List<List<int>>();

            for (var i = 0; i < count; i++)
            {
                processors.Add(new List<int>());
            }

            for (var i = 0; i < array.Count; i++)
            {
                var index = Utils.FindMinArrayIndex(processors);
                processors[index].Add(array[i]);
            }

            return processors;
        }

        static void Print(List<List<int>> matrix)
        {
            for (var i = 0; i < matrix.Count; i++)
            {
                Console.WriteLine($"{i + 1} - [{string.Join(", ", matrix[i])}] = {matrix[i].Sum()}");
            }

            var calc = CalculateItems(matrix);
            Console.WriteLine($"Min: {calc.Min} Max: {calc.Max} Delta: {calc.Delta}");
        }

        static void Main(string[] args)
        {
            var pFormatted = -1;
            var tFormatted = -1;
            var T1N = -1;
            var T2N = -1;

            while (pFormatted == -1 || tFormatted == -1 || T1N == -1 || T2N == -1)
            {
                Console.Write("Введите количество процессоров: ");
                var pInput = Console.ReadLine();
                Console.Write("Введите количество заданий: ");
                var tInput = Console.ReadLine();
                Console.Write("Введите T1: ");
                var T1 = Console.ReadLine();
                Console.Write("Введите T2: ");
                var T2 = Console.ReadLine();

                int.TryParse(pInput, out pFormatted);
                int.TryParse(tInput, out tFormatted);
                int.TryParse(T1, out T1N);
                int.TryParse(T2, out T2N);
            }

            List<List<int>> generated;
            string inputValue = "";

            while (inputValue == "")
            {
                Console.WriteLine("Выберите вариант: 1 - Критический; 2 - Случайный");
                Console.Write("> ");
                var answer = Console.ReadLine();

                if (answer == "1" || answer == "2")
                {
                    inputValue = answer;
                }
                else
                {
                    Console.WriteLine("Неправильный вариант!");
                }
            }

            if (inputValue == "1")
            {
                var rnd = new Random();
                var numbers = Utils.ListGenerator(tFormatted, () => rnd.Next(T1N, T2N));
                generated = CriticalFill(numbers, pFormatted);
            }
            else
            {
                var rnd = new Random();
                generated = Utils.ListGenerator(pFormatted, () => new List<int>());

                for (var i = 0; i < tFormatted; i++)
                {
                    var index = rnd.Next(0, pFormatted);
                    generated[index].Add(rnd.Next(T1N, T2N));
                }
            }

            Print(generated);
            Console.WriteLine("------------");
            Print(ProcessItems(generated));
        }

        static void Test()
        {
            /*
                Правильный вывод:
                1 - [10, 11, 11, 15] = 47
                2 - [13, 21, 14] = 48
                3 - [15, 15, 20] = 50
                Min: 47 Max: 50 Delta: 3
            */

            var generated = new List<List<int>>()
            {
                new List<int>() {21, 14, 13, 11, 15, 15},
                new List<int>() {10},
                new List<int>() {11, 15, 20}
            };

            Print(generated);
            Console.WriteLine("---------------");
            Print(ProcessItems(generated));
        }
    }
}