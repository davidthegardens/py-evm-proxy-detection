import { InfuraProvider } from '@ethersproject/providers'
import pkg from 'evm-proxy-detection';
const detectProxyTarget = pkg.default;

const address = process.argv[2];
const infura_key = process.argv[3];

const infuraProvider = new InfuraProvider(1, infura_key)
const requestFunc = ({ method, params }) => infuraProvider.send(method, params)

const target = await detectProxyTarget(
  address,
  requestFunc
)

console.log(JSON.stringify(target))