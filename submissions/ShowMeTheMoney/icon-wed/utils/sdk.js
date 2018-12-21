import { PROVIDER } from '../score/const';

export function getBalance(address) {
    const IconService = require('icon-sdk-js')
    const { HttpProvider } = IconService
    const iconService = new IconService(new HttpProvider(PROVIDER));
    const balance = iconService.getBalance(address).execute()
    return convertLoopToIcx(balance)
}

export function getTransactionResult(transactionHash) {
    const IconService = require('icon-sdk-js')
    const { HttpProvider } = IconService
    const iconService = new IconService(new HttpProvider(PROVIDER));
    return iconService.getTransactionResult(transactionHash).execute()
}

export function convertLoopToIcx(amount) {
    const IconService = require('icon-sdk-js')
    const { IconAmount } = IconService
    return IconAmount
        .of(amount, IconAmount.Unit.LOOP)
        .convertUnit(IconAmount.Unit.ICX)
        .toString()
}

export function convertIcxToLoop(amount) {
    const IconService = require('icon-sdk-js')
    const { IconAmount, IconConverter } = IconService
    return IconAmount
        .of(IconConverter.toBigNumber(amount), IconAmount.Unit.ICX)
        .convertUnit(IconAmount.Unit.LOOP)
}