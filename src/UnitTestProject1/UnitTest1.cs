using ConsoleApp1;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;

namespace UnitTestProject1
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            Example ex = new Example();
            (double quotient, double remainder) = ex.Divide(10, 2);
            Assert.AreEqual(5.0, quotient);
            Assert.AreEqual(0.0, remainder);

            (quotient, remainder) = ex.Divide(10, 3);
            Assert.AreEqual(3.0, quotient);
            Assert.AreEqual(1.0, remainder);
        }
    }
}
