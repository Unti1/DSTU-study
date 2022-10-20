using System;
using System.Collections.Generic;
using System.Linq;

namespace lab_4_cs
{
    public static class Utils
    {
        public static int FindListSum(IEnumerable<int> list)
        {
            return list.Sum();
        }

        public static int? GetFirstElementLowerThan(List<int> array, int lower)
        {
            for (var i = 0; i < array.Count; i++)
            {
                if (array[i] < lower)
                {
                    return array[i];
                }
            }

            return null;
        }

        public static List<List<T>> Clone<T>(List<List<T>> original)
            where T : ICloneable
        {
            var result = new List<List<T>>();

            foreach (List<T> innerList in original)
            {
                var innerResult = innerList.Select(item => (T) item.Clone()).ToList();
                result.Add(innerResult);
            }

            return result;
        }

        public static List<int> GetElementsLowerThan(List<int> list, int lower)
        {
            return list.FindAll(e => e < lower);
        }

        public static int FindMinArrayIndex(List<List<int>> arrays)
        {
            var index = 0;
            int? current = null;

            for (var i = 0; i < arrays.Count; i++)
            {
                var sum = arrays[i].Sum();

                if (!current.HasValue || current.Value > sum)
                {
                    index = i;
                    current = sum;
                }
            }

            return index;
        }

        public delegate T ListGeneratorCallback<out T>();
        
        public static List<T> ListGenerator<T>(int length, ListGeneratorCallback<T> cb)
        {
            var list = new List<T>();

            for (var i = 0; i < length; i++)
            {
                list.Add(cb());
            }

            return list;
        }
    }
}