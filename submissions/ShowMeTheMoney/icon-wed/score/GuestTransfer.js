import { convertIcxToLoop } from '../utils/sdk';

export default class GuestTransfer {

    constructor(url, nid) {
        const IconService = require('icon-sdk-js')
        const { HttpProvider } = IconService

        this.provider = new HttpProvider(url)
        this.iconService = new IconService(this.provider)
        this.nid = nid
    }
 
    // TODO
    // toRawTransction
    makeTransfer(guest, to, value, from) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallTransactionBuilder } = IconBuilder

        const timestamp = IconConverter.toHex((new Date()).getTime() * 1000)
        console.log(value)
        return IconConverter.toRawTransaction(new CallTransactionBuilder()
            .nid("0x3")
            .from(from)
            .to(to)
            .value(convertIcxToLoop(value))
            .stepLimit('0x87000000')
            .timestamp(timestamp)
            .method("congratulation")
            .params({
                'guest_information_json': this.guestDataToJson(guest),
            })
            .version("0x3")
            .build()
        )
    }

    makeRefundMealTicket(scoreAddress, address) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallTransactionBuilder } = IconBuilder

        const timestamp = IconConverter.toHex((new Date()).getTime() * 1000)
        return IconConverter.toRawTransaction(new CallTransactionBuilder()
            .nid(IconConverter.toBigNumber(this.nid))
            .from(address)
            .to(scoreAddress)
            .stepLimit(IconConverter.toBigNumber('0x87000000'))
            .timestamp(timestamp)
            .method("return_meal_ticket")
            .params({
                'account': address
            })
            .version(IconConverter.toBigNumber(3))
            .build()
        )
    }


    transfer(guest, to, value, wallet) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter, SignedTransaction } = IconService
        const { CallTransactionBuilder } = IconBuilder

        const timestamp = (new Date()).getTime() * 1000
        const transaction = new CallTransactionBuilder()
                .nid(IconConverter.toBigNumber(this.nid))
                .from(wallet.getAddress())
                .to(to)
                .value(value)
                .stepLimit(IconConverter.toBigNumber('0x87000000'))
                .timestamp(timestamp)
                .method("congratulation")
                .params({
                    'guest_information_json': this.guestDataToJson(guest),
                })
                .version(IconConverter.toBigNumber(3))
                .build();
        const signedTransaction = new SignedTransaction(transaction, wallet)
        return this.iconService.sendTransaction(signedTransaction, wallet).execute()                
    }

    returnMealTicket(scoreAddress, address, wallet) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter, SignedTransaction } = IconService
        const { CallTransactionBuilder } = IconBuilder

        const timestamp = (new Date()).getTime() * 1000
        const transaction = new CallTransactionBuilder()
                .nid(IconConverter.toBigNumber(this.nid))
                .from(wallet.getAddress())
                .to(scoreAddress)
                .stepLimit(IconConverter.toBigNumber('0x87000000'))
                .timestamp(timestamp)
                .method("return_meal_ticket")
                .params({
                    'account': address
                })
                .version(IconConverter.toBigNumber(3))
                .build();
        const signedTransaction = new SignedTransaction(transaction, wallet)
        return this.iconService.sendTransaction(signedTransaction, wallet).execute()                
    }

    guestDataToJson(guest) {
        const IconService = require('icon-sdk-js')
        const { IconConverter } = IconService

        guest.name = IconConverter.toHex(guest.name)
        guest.message = IconConverter.toHex(guest.message)
        return JSON.stringify(guest)
    }

    returnMealTicket(scoreAddress, address, wallet) {
        const timestamp = (new Date()).getTime() * 1000
        const transaction = new CallTransactionBuilder()
                .nid(IconConverter.toBigNumber(this.nid))
                .from(wallet.getAddress())
                .to(scoreAddress)
                .stepLimit(IconConverter.toBigNumber('0x87000000'))
                .timestamp(timestamp)
                .method("return_meal_ticket")
                .params({
                    'account': address
                })
                .version(IconConverter.toBigNumber(3))
                .build();
        const signedTransaction = new SignedTransaction(transaction, wallet)
        return this.iconService.sendTransaction(signedTransaction, wallet).execute()                
    }

    getTempGuest() {
        return {
            'name': '송화중',
            'message': '성지영',
            'attend': true,
            'secret': true,
            'host': 0,  // 0: 신랑, 1: 신부
            'ticket_amount': 2
        }
    }
}