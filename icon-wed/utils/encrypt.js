import CryptoJS from 'crypto-js'
import { setItem, getItem } from './storage';
import ecies from 'eth-ecies'

export function getEncryptionKey(password) {
    const { IconWallet } = require('icon-sdk-js')
    const wallet = IconWallet.create()
    const stored = JSON.stringify(wallet.store(password));    
    const encrypted = CryptoJS.AES.encrypt(stored, password).toString()
    setItem('keyData', encrypted)
    return wallet.getPublicKey()
}

export function getDecryptionKey(password) {
    const { IconWallet } = require('icon-sdk-js')
    const encrypted = getItem('keyData')
    const decrypted = CryptoJS.AES.decrypt(encrypted, password).toString(CryptoJS.enc.Utf8)
    const wallet = IconWallet.loadKeystore(decrypted, password)
    return wallet.getPrivateKey()
}

export function encrypt(plain, encryptionKey) {
    return ecies.encrypt(Buffer.from(encryptionKey, 'hex'), plain)
}

export function decrypt(encrypted, decryptionKey) {
    return ecies.decrypt(Buffer.from(decryptionKey, 'hex'), encrypted).toString()
}