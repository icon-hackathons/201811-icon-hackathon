import { convertLoopToIcx } from '../utils/sdk';

export default class WeddingScore {

    constructor(url, nid, scoreAddress) {
        const IconService = require('icon-sdk-js')
        const { HttpProvider } = IconService

        this.provider = new HttpProvider(url)
        this.iconService = new IconService(this.provider)
        this.scoreAddress = scoreAddress
        this.nid = nid
    }

    information() {
        const IconService = require('icon-sdk-js')
        const { IconBuilder } = IconService
        const { CallBuilder } = IconBuilder

        const result = this.iconService.call(new CallBuilder()
                .to(this.scoreAddress)
                .method('information')
                .build()).execute(false);
        return this.convertToInformation(result)
    }

    getPublicKey() {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallBuilder } = IconBuilder

        return this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method('get_public_key')
            .build()).execute();   
    }

    getGuestsCount() {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallBuilder } = IconBuilder

        const result = this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method('get_guests_count')
            .build()).execute(false);
        return IconConverter.toBigNumber(result).toString()    
    }

    getMealTicketInfo() {
        const IconService = require('icon-sdk-js')
        const { IconBuilder } = IconService
        const { CallBuilder } = IconBuilder

        const result = this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method('get_meal_ticket_info')
            .build()).execute(false);
        return this.convertToMealInfo(result)
    }

    makeSetWeddingScoreAddress(managerAddress, address, from) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallTransactionBuilder } = IconBuilder

        const timestamp = (new Date()).getTime() * 1000
        return new CallTransactionBuilder()
                .nid(IconConverter.toBigNumber(this.nid))
                .from(from)
                .to(managerAddress)
                .stepLimit(IconConverter.toBigNumber('0x87000000'))
                .timestamp(timestamp)
                .method("set_wedding_score_address")
                .params({
                    'wedding_score': this.scoreAddress,
                    'address': address
                })
                .version(IconConverter.toBigNumber(3))
                .build();
    }

    setWeddingScoreAddress(managerAddress, address, wallet) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter, SignedTransaction } = IconService
        const { CallTransactionBuilder } = IconBuilder

        const timestamp = (new Date()).getTime() * 1000
        const transaction = new CallTransactionBuilder()
                .nid(IconConverter.toBigNumber(this.nid))
                .from(wallet.getAddress())
                .to(managerAddress)
                .stepLimit(IconConverter.toBigNumber('0x87000000'))
                .timestamp(timestamp)
                .method("set_wedding_score_address")
                .params({
                    'wedding_score': this.scoreAddress,
                    'address': address
                })
                .version(IconConverter.toBigNumber(3))
                .build();
        const signedTransaction = new SignedTransaction(transaction, wallet)
        return this.iconService.sendTransaction(signedTransaction, wallet).execute()                
    }

    getGroomGuests(offset, count) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallBuilder } = IconBuilder

        const guests = this.iconService.call(new CallBuilder()
                .to(this.scoreAddress)
                .method('get_groom_guests')
                .params({
                    'offset': IconConverter.toBigNumber(offset),
                    'count': IconConverter.toBigNumber(count)
                })
                .build()).execute(false)

        var result = []
        console.log(guests)
        for (var index in guests) {
            result.push(this.convertToGuest(guests[index]))
        }
        return result
    }

    getBrideGuests(offset, count) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallBuilder } = IconBuilder

        const guests = this.iconService.call(new CallBuilder()
                .to(this.scoreAddress)
                .method('get_bride_guests')
                .params({
                    'offset': IconConverter.toBigNumber(offset),
                    'count': IconConverter.toBigNumber(count)
                })
                .build()).execute(false)

        var result = []
        console.log(guests)
        for (var index in guests) {
            result.push(this.convertToGuest(guests[index]))
        }
        return result
    }

    getMealTicketCount(address) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallBuilder } = IconBuilder

        const result = this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method('get_meal_ticket_count')
            .params({
                'account': address
            })
            .build()).execute(false);
        return IconConverter.toBigNumber(result).toString()    
    }

    getAmountRaised() {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallBuilder } = IconBuilder

        const result = this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method('get_amount_raised')
            .build()).execute(false);
        return convertLoopToIcx(IconConverter.toBigNumber(result))
    }

    getPublicKey() {
        const IconService = require('icon-sdk-js')
        const { IconBuilder } = IconService
        const { CallBuilder } = IconBuilder

        return this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method('get_public_key')
            .build()).execute();   
    }

    setPublicKey(publicKey, wallet) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter, SignedTransaction } = IconService
        const { CallTransactionBuilder } = IconBuilder

        console.log('publicKey:', publicKey)
        const timestamp = (new Date()).getTime() * 1000
        const transaction = new CallTransactionBuilder()
                .nid(IconConverter.toBigNumber(this.nid))
                .from(wallet.getAddress())
                .to(this.scoreAddress)
                .stepLimit(IconConverter.toBigNumber('0x87000000'))
                .timestamp(timestamp)
                .method('set_public_key')
                .params({
                    'public_key': Buffer.from(publicKey).toString('hex')
                })
                .version(IconConverter.toBigNumber(3))
                .build();
        const signedTransaction = new SignedTransaction(transaction, wallet)
        return this.iconService.sendTransaction(signedTransaction, wallet).execute()                
    }

    convertToGuest(guest) {
        const IconService = require('icon-sdk-js')
        const { IconConverter } = IconService

        console.log(guest)
        return {
            'address': guest.address,
            'amount': IconConverter.toBigNumber(guest.amount).toString(),
            'hash': guest.hash,
            'message': this.hexToString(guest.message),
            'name': this.hexToString(guest.name),
            'timestamp': IconConverter.toBigNumber(guest.timestamp).toString(),
            'secret': guest.secret
        }
    }

    convertToInformation(information) {
        const IconService = require('icon-sdk-js')
        const { IconConverter } = IconService

        return {
            'groom_name': this.hexToString(information.groom_name),
            'bride_name': this.hexToString(information.bride_name),
            'groom_father_name': this.hexToString(information.groom_father_name),
            'groom_mother_name': this.hexToString(information.groom_mother_name),
            'bride_father_name': this.hexToString(information.bride_father_name),
            'bride_mother_name': this.hexToString(information.bride_mother_name),
            'invitation_message': this.hexToString(information.invitation_message),
            'wedding_date': IconConverter.toBigNumber(information.wedding_date).toString(),
            'wedding_date_str': this.hexToString(information.wedding_date_str),
            'wedding_place_name': this.hexToString(information.wedding_place_name),
            'wedding_place_address': this.hexToString(information.wedding_place_address),
            'wedding_photo_url': this.hexToString(information.wedding_photo_url)
        }
    }

    makeWithdraw(address, from) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { CallTransactionBuilder } = IconBuilder

        const timestamp = (new Date()).getTime() * 1000
        return IconConverter.toRawTransaction(new CallTransactionBuilder()
            .nid(IconConverter.toBigNumber(this.nid))
            .from(from)
            .to(this.scoreAddress)
            .stepLimit(IconConverter.toBigNumber('0x87000000'))
            .timestamp(timestamp)
            .method('withdraw')
            .params({
                'account': address
            })
            .version(IconConverter.toBigNumber(3))
            .build()
        )
    }

    convertToMealInfo(mealInfo) {
        const IconService = require('icon-sdk-js')
        const { IconConverter } = IconService

        var result = {}
        for (var key in mealInfo) {
            result[key] = IconConverter.toBigNumber(mealInfo[key]).toString()
        }    
        return result
    }

    hexToString(value) {
        return Buffer.from(this.stripHexPrefix(value), 'hex').toString()
    }

    stripHexPrefix = (value) => {
        if (!value) return ''
        return value.replace('0x', '');
    };
    

    getWeddingScoreAddress(account) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder } = IconService
        const { CallBuilder } = IconBuilder

        return this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method('get_wedding_score_address')
            .params({
                'owner': account
            })
            .build()).execute(false)
    }

    getWeddingScoreCode() {
        const IconService = require('icon-sdk-js')
        const { IconBuilder } = IconService
        const { CallBuilder } = IconBuilder

        return this.iconService.call(new CallBuilder()
                .to(this.scoreAddress)
                .method('get_wedding_score_code')
                .build()).execute(false);
    }

    deployWeddingScore(params, wallet) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter, SignedTransaction } = IconService
        const { DeployTransactionBuilder } = IconBuilder

        const { information, meal_ticket_count, public_key } = params
        const timestamp = (new Date()).getTime() * 1000
        const contentType = 'application/zip'
        const content = this.getWeddingScoreCode()
        const transaction =  new DeployTransactionBuilder()
                .nid(IconConverter.toBigNumber(this.nid))
                .from(wallet.getAddress())
                .to('cx0000000000000000000000000000000000000000')
                .stepLimit(IconConverter.toBigNumber('0x87000000'))
                .timestamp(timestamp)
                .contentType(contentType)
                .content(content)
                .params({
                    'information_json': this.convertWeddingInformation(information),
                    'manager_score': this.scoreAddress,
                    'meal_ticket_count': meal_ticket_count,
                    'public_key': Buffer.from(public_key).toString('hex')
                })
                .version(IconConverter.toBigNumber(3))
                .build()
        const signedTransaction = new SignedTransaction(transaction, wallet)
        return this.iconService.sendTransaction(signedTransaction, wallet).execute()
    }

    convertWeddingInformation(information) {
        const IconService = require('icon-sdk-js')
        const { IconConverter } = IconService

        var result = {}
        for (var key in information) {
            result[key] = IconConverter.toHex(information[key])
        }
        console.log(information, result)
        return JSON.stringify(result)
    }

    getTempInformation() {
        return {
            'groom_name': '송화중',
            'bride_name': '성지영',
            'groom_father_name': '송병현',
            'groom_mather_name': '정영옥',
            'bride_father_name': '성용호',
            'bride_mather_name': '신학심',
            'invitaion_message': "서로가 마주보며 다져온 사랑을 \n" +
                                "이제 함께 한 곳을 바라보며 걸어갈 수 있는 \n" +
                                "큰 사랑으로 키우고자 합니다.\n" +
                                "저희 두 사람이 사랑의 이름으로 지켜나갈 수 있게\n" +
                                "앞 날을 축복해주시면 감사하겠습니다.",
            'wedding_date': 1542520331000000,
            'wedding_place_name': '헤레이스',
            'wedding_place_address': '서울 영등포구 당산동3가 81'
        }
    }

}