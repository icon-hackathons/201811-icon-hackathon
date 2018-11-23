import { convertLoopToIcx } from '../utils/sdk';

export default class TokenScore {

    constructor(url, nid, scoreAddress) {
        const IconService = require('icon-sdk-js')
        const { HttpProvider } = IconService

        this.provider = new HttpProvider(url)
        this.iconService = new IconService(this.provider)
        this.scoreAddress = scoreAddress
        this.nid = nid
    }
    
    balanceOf(address) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder } = IconService
        const { CallBuilder } = IconBuilder

        const balance = this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method('balanceOf')
            .params({
                '_owner': address
            })
            .build()).execute(false);
        return convertLoopToIcx(balance)
    }

    transfer(to, value, wallet) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter, SignedTransaction } = IconService
        const { CallTransactionBuilder } = IconBuilder

        const timestamp = (new Date()).getTime() * 1000
        const transaction = new CallTransactionBuilder()
                .nid(IconConverter.toBigNumber(this.nid))
                .from(wallet.getAddress())
                .to(this.scoreAddress)
                .stepLimit(IconConverter.toBigNumber('0x87000000'))
                .timestamp(timestamp)
                .method("transfer")
                .params({
                    '_to': to,
                    '_value': value
                })
                .version(IconConverter.toBigNumber(3))
                .build();
        const signedTransaction = new SignedTransaction(transaction, wallet)
        return this.iconService.sendTransaction(signedTransaction, wallet).execute()                
    }

}