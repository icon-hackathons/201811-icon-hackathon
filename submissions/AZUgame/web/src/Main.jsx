import React, { Component } from "react";
import Builder from "./sdk";
import Slider from "react-rangeslider";
import Header from "./Header";
import Popup from "./Popup";
import * as api from "./api";

class Main extends Component {
	constructor(props, context) {
		super(props, context);
		this.state = {
			popupContents: {
				title: "",
				type: "",
				contents: {
					content1: "",
					content2: ""
				}
			},
			popup: false,
			address: localStorage.getItem("address"),
			bet: 0,
			value: 2,
			get: 0,
			dividend: {
				rollUnder: 2,
				payOut: 98,
				chance: 1
			}
		};
	}
	componentDidMount() {
		this.builder = new Builder();
		if (localStorage.getItem("address")) {
			const amount = this.builder.getAmount(this.state.address);
			this.setState({ amount });
		}
	}
	componentDidUpdate(prevProps, prevState) {
		if (
			prevState.popup !== this.state.popup &&
			this.state.popupContents.type === "result"
		) {
			const amount = this.builder.getAmount(this.state.address);
			this.setState({ amount });
		}
	}

	onChange = e => {
		this.setState(
			{
				bet: e.target.value
			},
			() => {
				this.handleChangeComplete();
			}
		);
	};
	onClickPlay = async () => {
		const { bet, address, amount } = this.state;
		const { rollUnder } = this.state.dividend;
		if (Number(bet) > Number(amount)) {
			this.setState({
				popup: true,
				popupContents: {
					title: "Low balance",
					type: "alert",
					contents: { content1: "There is not enough balance" }
				}
			});
			return;
		}

		const value = `0x${(bet * 1000000000000000000).toString(16)}`;
		const roll_under = `0x${rollUnder.toString(16)}`;

		try {
			const readyToBetRes = await api.readyToBet(address);
			const { houseHash, id } = readyToBetRes.data;
			const betParams = {
				address,
				amount: value,
				roll_under,
				house_hash: houseHash,
				player_seed: "p_seed"
			};
			const betRes = await this.builder.bet(betParams);
			const tx = await api.sendTransaction(betRes);
			const getIndex = () => {
				const index = new Promise((resolve, reject) => {
					setTimeout(() => {
						const txRes = this.builder.getTransactionResult(tx.result);
						if (txRes.status === 1) {
							resolve(txRes.eventLogs[0].indexed[1]);
						}
					}, 2000);
				});
				return index;
			};
			const index = await getIndex();
			if (index) {
				const rollData = {
					address,
					index: index,
					params: {
						houseHash: houseHash,
						houseHashId: id
					}
				};
				const rollRes = await api.roll(rollData);
				console.log(rollRes);
				if (rollRes.data === true) {
					this.setState(
						{
							popupContents: {
								title: "YOU WIN!",
								type: "result",
								contents: {
									content2: this.state.get
								}
							}
						},
						() => {
							this.setState({
								popup: true
							});
						}
					);
				} else if (rollRes.data === false) {
					this.setState(
						{
							popupContents: {
								title: "YOU LOSE!",
								type: "result",
								contents: {
									content2: 0
								}
							}
						},
						() => {
							this.setState({
								popup: true
							});
						}
					);
				}
			} else {
				this.setState({
					popup: true,
					popupContents: {
						title: "Error",
						type: "alert",
						contents: {
							content1: "Play will be void"
						}
					}
				});
			}
		} catch (error) {
			console.error(error);
			this.setState({
				popup: true,
				popupContents: {
					title: "Error",
					type: "alert",
					contents: {
						content1: "Play will be void"
					}
				}
			});
		}
	};

	onClickClose = () => {
		this.setState({
			popup: false
		});
	};
	handleChangeStart = () => {};

	handleChange = value => {
		this.setState({
			value: value
		});
	};

	handleChangeComplete = () => {
		const { value, bet } = this.state;
		const rollUnder = value;
		const payOut = (100 / (value - 1)) * 0.98;
		const chance = value - 1;
		const get = payOut * bet;
		this.setState({
			get: get,
			dividend: {
				...this.state.dividend,
				rollUnder: rollUnder,
				payOut: payOut,
				chance: chance
			}
		});
	};
	render() {
		const { value, bet, get } = this.state;
		const { rollUnder, payOut, chance } = this.state.dividend;
		return (
			<main>
				<Header />
				{this.state.popup ? (
					<Popup
						contents={this.state.popupContents}
						onClickClose={this.onClickClose}
					/>
				) : (
					""
				)}
				<div className="balance">
					<p>{this.state.amount ? this.state.amount.toFixed(2) : 0}P</p>
				</div>
				<div className="curtain-left" />
				<div className="curtain-right" />
				<div className="chips">
					<div />
					<div />
					<div />
					<div />
				</div>
				<div className="dices">
					<div />
					<div />
				</div>

				<div className="box">
					<div className="welcome">
						<span />
						<span />
						<span />
						<span />
						<span />
						<span />
						<span />
					</div>
					<div className="title" />
					<p className="box-top-p">
						Choose <strong>bet number!</strong>
					</p>
					<div className="slider">
						<p className="start">0</p>
						<p className="end">100</p>
						<Slider
							min={2}
							max={96}
							value={value}
							onChangeStart={this.handleChangeStart}
							onChange={this.handleChange}
							onChangeComplete={this.handleChangeComplete}
						/>
					</div>
					<div className="dividend">
						<div className="dividend-content">
							<p>ROLL UNDER</p>
							<div className="value">{rollUnder}</div>
						</div>
						<div className="dividend-content">
							<p>PAY OUT</p>
							<div className="value">{payOut.toFixed(2)}x</div>
						</div>
						<div className="dividend-content">
							<p>WINNING CHANCE</p>
							<div className="value">{chance}%</div>
						</div>
					</div>
					<div className="amount">
						<p className="icon-logo" />
						<p className="icx">ICX</p>
						<input value={bet} onChange={this.onChange} />
						<p className="expected">you will get {get.toFixed(2)} ICX</p>
					</div>
					<button onClick={this.onClickPlay} className="play-btn" />
				</div>
			</main>
		);
	}
}

export default Main;
