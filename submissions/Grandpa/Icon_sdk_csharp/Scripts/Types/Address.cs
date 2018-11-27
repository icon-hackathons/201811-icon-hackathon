using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace IconSDK.Types
{
    public abstract class Address : Bytes
    {
        public override uint Size => 20;

        public Address(IEnumerable<byte> bytes)
            : base(bytes)
        {

        }

        public Address(string hex)
            : base(hex)
        {

        }

        public Address(BigInteger value)
            : base(value)
        {

        }
    }

    public class ExternalAddress : Address
    {
        public override string Prefix => "hx";

        public ExternalAddress(IEnumerable<byte> bytes)
            : base(bytes)
        {

        }

        public ExternalAddress(string hex)
            : base(hex)
        {

        }

        public ExternalAddress(BigInteger value)
            : base(value)
        {

        }

        public string ToHexhx()
        {
            return ToString();
        }
    }

    public class ContractAddress : Address
    {
        public override string Prefix => "cx";

        public ContractAddress(IEnumerable<byte> bytes)
            : base(bytes)
        {

        }

        public ContractAddress(string hex)
            : base(hex)
        {

        }

        public ContractAddress(BigInteger value)
            : base(value)
        {

        }

        public string ToHexcx()
        {
            return ToString();
        }
    }
}
