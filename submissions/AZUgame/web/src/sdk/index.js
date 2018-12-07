import IconService, {
	IconConverter,
	IconAmount,
	IconBuilder
} from "icon-sdk-js";

function convertLoopToIcx(amount) {
	return IconAmount.of(amount, IconAmount.Unit.LOOP)
		.convertUnit(IconAmount.Unit.ICX)
		.toString();
}

export default class Builder {
	constructor() {
		const { HttpProvider } = IconService;

		this.provider = new HttpProvider("https://bicon.net.solidwallet.io/api/v3");
		this.iconService = new IconService(this.provider);
		this.scoreAddress = "cxac3b709b17cb54fbc8cd1c0e732f54aa994628ad";
		this.nid = "0x3";
	}
	getTransactionResult = txHash => {
		return this.iconService.getTransactionResult(txHash).execute();
	};
	bet = payload => {
		const { CallTransactionBuilder } = IconBuilder;
		const { address, amount, roll_under, house_hash, player_seed } = payload;
		let params = {
			amount,
			roll_under,
			house_hash,
			player_seed
		};
		const transaction = new CallTransactionBuilder();
		const result = transaction
			.nid(this.nid)
			.from(address)
			.to(this.scoreAddress)
			.nonce("0x1")
			.value("0x0")
			.stepLimit("0x87000000")
			.timestamp(`0x${(new Date().getTime() * 1000).toString(16)}`)
			.version("0x3")
			.method("bet")
			.params(params)
			.build();
		return result;
	};

	getAmount = address => {
		const { CallBuilder } = IconBuilder;
		const res = this.iconService
			.call(
				new CallBuilder()
					.from(address)
					.to(this.scoreAddress)
					.method("get_available_amount")
					.params({
						account: address
					})
					.build()
			)
			.execute();
		return Number(convertLoopToIcx(IconConverter.toBigNumber(res)));
	};
}
