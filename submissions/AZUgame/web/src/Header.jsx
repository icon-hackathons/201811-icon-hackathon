import React, { Component } from "react";
import { getWalletAddress } from "./api";
class Header extends Component {
	state = {
		login: false
	};

	onClick = async () => {
		const address = await getWalletAddress();
		if (address) {
			await localStorage.setItem("address", address);
			this.setState({
				login: true
			});
		}
	};

	render() {
		return (
			<header>
				<div className="logo" />
				{localStorage.getItem("address") || this.state.login === true ? (
					<div className="user">
						<span>{localStorage.getItem("address")}</span>
					</div>
				) : (
					<button onClick={this.onClick} />
				)}
			</header>
		);
	}
}
export default Header;
