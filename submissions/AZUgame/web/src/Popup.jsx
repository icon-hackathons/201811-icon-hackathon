import React, { Component } from "react";
import cn from "classnames";

class Popup extends Component {
	render() {
		const { contents, onClickClose } = this.props;
		return (
			<div className="popup-container">
				<div className="popup">
					<h3>{contents.title}</h3>
					{contents.type === "alert" ? (
						<p className="alert-txt">{contents.contents.content1}</p>
					) : (
						<div className="result">
							<p className="result-txt">
								You got {contents.contents.content2.toFixed(2)} ICX
							</p>
						</div>
					)}
					<button className="ok-btn" onClick={onClickClose} />
				</div>
			</div>
		);
	}
}

export default Popup;
