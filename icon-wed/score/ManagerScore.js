export default class ManagerScore {

    constructor(url, nid, scoreAddress) {
        const IconService = require('icon-sdk-js')
        const { HttpProvider } = IconService
        
        this.provider = new HttpProvider(url)
        this.iconService = new IconService(this.provider)
        this.scoreAddress = scoreAddress
        this.nid = nid
    }

    getWeddingScoreAddress(account) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder } = IconService
        const { CallBuilder } = IconBuilder
        
        return this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method("get_wedding_score_address")
            .params({
                "owner": account
            })
            .build()).execute(false)
    }

    getWeddingScoreCode() {
        const IconService = require('icon-sdk-js')
        const { IconBuilder } = IconService
        const { CallBuilder } = IconBuilder
        
        return this.iconService.call(new CallBuilder()
            .to(this.scoreAddress)
            .method("get_wedding_score_code")
            .build()).execute(false);
    }

    makeDepolyTransaction(params, from, toRawTransaction) {
        const IconService = require('icon-sdk-js')
        const { IconBuilder, IconConverter } = IconService
        const { DeployTransactionBuilder } = IconBuilder

        console.log(params, from, toRawTransaction)

        const { information, meal_ticket_count, public_key } = params
        const timestamp = IconConverter.toHex((new Date()).getTime() * 1000)
        const contentType = "application/zip"
        const content = this.getWeddingScoreCode()
        const transaction = new DeployTransactionBuilder()
            .nid(IconConverter.toBigNumber(this.nid))
            .from(from)
            .to("cx0000000000000000000000000000000000000000")
            .stepLimit(IconConverter.toBigNumber("0x87000000"))
            .timestamp(timestamp)
            .contentType(contentType)
            .content(content)
            .params({
                'information_json': this.weddingInformationToJson(information),
                'manager_score': this.scoreAddress,
                'meal_ticket_count': IconConverter.toHex(meal_ticket_count),
                'public_key': Buffer.from(public_key).toString('hex')
            })
            .version(IconConverter.toBigNumber(3))
            .build()

        return toRawTransaction ? IconConverter.toRawTransaction(transaction) : transaction
    }

    deployWeddingScore(params, wallet) {
        const IconService = require('icon-sdk-js')
        const { SignedTransaction } = IconService
        
        const transaction = this.makeDepolyTransaction(params, wallet.getAddress())
        const signedTransaction = new SignedTransaction(transaction, wallet)
        return this.iconService.sendTransaction(signedTransaction, wallet).execute()
    }

    weddingInformationToJson(information) {
        const IconService = require('icon-sdk-js')
        const { IconConverter } = IconService

        var result = {}
        for (var key in information) {
            result[key] = IconConverter.toHex(information[key])
        }
        return JSON.stringify(result)
    }

    getTempInformation() {
        return {
            'groom_name': '송화중',
            'bride_name': '성지영',
            'groom_father_name': '송병현',
            'groom_mother_name': '정영옥',
            'bride_father_name': '성용호',
            'bride_mother_name': '신학심',
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