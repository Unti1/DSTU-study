using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.VisualBasic;

namespace kod
{
    class Program
    {
        static (string, List<string>, List<int>, string[], int, List<List<int>>) koding1(string arg1)
        {
            string s = "";
            string tempp = arg1;
            string sk = "";
            string primer = "";




            Console.WriteLine("\n---------------------------");
            Console.WriteLine(arg1);

            for (int i = 0; i < tempp.Length; i++)
            {
                if (tempp[i] == '0' || tempp[i] == '1')
                {
                    s += tempp[i];
                    continue;
                }

                s += Convert.ToString(Convert.ToByte(tempp[i]), 2);
            }

            Console.WriteLine(s);

            primer = s;
            primer = primer.Insert(0, "X").Insert(1, "X");

            sk = s;
            s = s.Insert(0, "0").Insert(1, "0");
            int numBit = 2;

            for (int i = 4, j = 3; i < s.Length; i = (int)Math.Pow(2, j), j++)
            {
                numBit++;
                s = s.Insert(i - 1, "0");
                primer = primer.Insert(i - 1, "X");
            }
            Console.WriteLine("Кол-во контрольных бит: {0} ", numBit);
            Console.WriteLine(s);
            Console.WriteLine(primer);

            Console.WriteLine();

            List<string> s_list = new List<string>(new string[numBit]);

            int x = s.Length;

            for (int i = 0; i < s.Length / 2; i++)
                s_list[0] += "0";
            for (int i = 0; i < s.Length; i = i + 2)
                s_list[0] = s_list[0].Insert(i, "1");
            Console.WriteLine(s_list[0]);

            for (int k = 1; k < numBit; k++)
            {
                if (numBit == 1)
                {
                    for (int i = 0; i < s.Length / 2; i++)
                        s_list[1] += "0";
                    for (int i = 1; i < s.Length; i = i + 4)
                        s_list[1] = s_list[1].Insert(i, "11");
                    if (s_list[1].Length > s_list[0].Length)
                    {
                        s_list[1] = s_list[1].Remove(s_list[1].Length - 1);
                    }
                    else if (s_list[1].Length < s_list[0].Length)
                    {
                        s_list[1] += "0";
                    }
                    Console.WriteLine(s_list[1]);

                    continue;
                }

                s_list[k] = s;
                s_list[k] = s_list[k].Replace('1', '0');

                for (int i = (int)Math.Pow(2, k) - 1; i < s.Length; i = i + (int)Math.Pow(2, k + 1))
                {
                    s_list[k] = s_list[k].Insert(i, new String('1', (int)Math.Pow(2, k)));
                }
                if (s_list[k].Length > s_list[k - 1].Length)
                {
                    int raznica = s_list[k].Length - s_list[k - 1].Length;
                    s_list[k] = s_list[k].Remove(s_list[k].Length - raznica);
                }
                Console.WriteLine(s_list[k]);

            }

            var sBoss_list = new List<List<int>>();
            int[] sBoss = s.Select(ch => int.Parse(ch.ToString())).ToArray();


            for (int i = 0; i < numBit; i++)
            {
                sBoss_list.Add(new List<int>());
                sBoss_list[i] = s_list[i].Select(ch => int.Parse(ch.ToString())).ToList();
            }



            string[] tem = new string[numBit];
            List<int> temp = new List<int>(numBit);

            for (int i = 0; i < numBit; i++)
            {
                temp.Add(0);
                for (int j = 0; j < s.Length; j++)
                    temp[i] += sBoss[j] * sBoss_list[i][j];
                if (temp[i] > 1)
                    tem[i] = Convert.ToString(temp[i] % 2);
                else
                    tem[i] = Convert.ToString(temp[i]);
                Console.WriteLine($"r{i + 1} = " + tem[i]);
            }



            for (int i = 1, j = 1, k = 0; i < sk.Length; i = (int)Math.Pow(2, j), j++, k++)
            {
                sk = sk.Insert(i - 1, tem[k]);
            }
            Console.WriteLine(sk);

            return (sk, s_list, temp, tem, numBit, sBoss_list);
        }

        static string decoding(string s, string res, List<string> s_list, List<int> temp, string[] tem, int numBit, List<List<int>> sBoss_list)
        {
            string was = "";
            Console.WriteLine("\n---------------------------");
            for (int i = 0; i < s_list.Count; i++)
            {
                Console.WriteLine(s_list[i]);
            }


            was = s;
            int[] sBossDecode = s.Select(ch => int.Parse(ch.ToString())).ToArray();

            for (int i = 0; i < temp.Count; i++)
            {
                temp[i] = 0;
            }

            for (int i = 0; i < numBit; i++)
            {
                for (int j = 0; j < s.Length; j++)
                    temp[i] += sBossDecode[j] * sBoss_list[i][j];
                if (temp[i] > 1)
                    tem[i] = Convert.ToString(temp[i] % 2);
                else
                    tem[i] = Convert.ToString(temp[i]);
                Console.WriteLine($"r{i + 1} = " + tem[i]);
            }



            int plus = 0;

            for (int i = 0; i < tem.Length; i++)
            {
                if (tem[i] != "0")
                {
                    plus += (int)Math.Pow(2, i);
                }
            }

            if (plus != 0)
            {
                Console.WriteLine("Ошибка на {0} позиции", plus);

                if (s[plus - 1] == '1')
                {
                    s = s.Remove(plus - 1, 1).Insert(plus - 1, "0");
                }
                else
                {
                    s = s.Remove(plus - 1, 1).Insert(plus - 1, "1");
                }

                Console.WriteLine("Было\n{0}", was);
                Console.WriteLine("Стало\n{0}", s);
            }

            string res2 = s;

            s = s.Remove(0, 1);
            s = s.Remove(0, 1);
            s = s.Remove(1, 1);
            s = s.Remove(4, 1);

            string result = Convert.ToString((char)Convert.ToInt32(s, 2));
            return res2 == res ? result : "*";

        }



        static void Main(string[] args)
        {
            Console.WriteLine("Введите сообщение: ");
            string str = Console.ReadLine();
            char[] str_list = str.ToCharArray();
            List<(string, List<string>, List<int>, string[], int, List<List<int>>)> str_list2 = new List<(string, List<string>, List<int>, string[], int, List<List<int>>)>();
            str = "";

            for (int i = 0; i < str_list.Length; i++)
            {
                str_list2.Add(koding1(str_list[i].ToString()));
                str += str_list2[i].Item1;

            }

            Console.WriteLine(str);
            string str2 = str;

            var count = 0;

            string s3 = "";

            Random rnd = new Random();

            foreach (var item in str_list2)
            {
                int x = rnd.Next(0, 3);
                string temp = "";
                Console.WriteLine(str2.Substring(count, 11).Substring(0, 2));

                switch (x)
                {

                    case 0:

                        temp = str2.Substring(count, 11);
                        break;

                    case 1:
                        temp = str2.Substring(count, 11)[0] == '0' ? "1" + str2.Substring(count, 11).Substring(1) : "0" + str2.Substring(count, 11).Substring(1);
                        break;
                    case 2:
                        temp = str2.Substring(count, 11).Substring(0, 2) == "00" ? "11" + str2.Substring(count, 11).Substring(2) : str2.Substring(count, 11).Substring(0, 2) == "01" ? "10" + str2.Substring(count, 11).Substring(2) : str2.Substring(count, 11).Substring(0, 2) == "10" ? "01" + str2.Substring(count, 11).Substring(2) : "11" + str2.Substring(count, 11).Substring(1);
                        break;
                    case 3:
                        temp = rnd.Next(0, 1) == 0 ? "101" + str2.Substring(count, 11).Substring(3) : "100" + str2.Substring(count, 11).Substring(3);
                        break;

                }

                s3 += Program.decoding(temp, item.Item1, item.Item2, item.Item3, item.Item4, item.Item5, item.Item6);
                count += 11;
            }
            Console.WriteLine("Полученное сообщение: " + s3);

            Console.ReadKey();

        }
    }

}
