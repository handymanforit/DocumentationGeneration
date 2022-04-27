using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    /// <summary>
    /// A simple example class with one method which divides two numbers.
    /// </summary>
    public class Example
    {

        /// <summary>
        /// Divides the specified dividend by the divisor, returning the quotient and the remainder as a Tuple.
        /// </summary>
        /// <param name="dividend">The dividend - the number which will be divided by the divisor.</param>
        /// <param name="divisor">The divisor - the number by which the dividend will be divided.</param>
        /// <returns>(quotient, remainder)</returns>
        public (double quotient, double remainder) Divide(int dividend, int divisor)
        {
            return (dividend / divisor, dividend % divisor);
        }
    }
}

