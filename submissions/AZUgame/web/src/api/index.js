import axios from "axios";

const host = "http://54.180.14.6:8080/";
// const host = "http://10.130.109.224:8080/";

const scoreAddress = "cxac3b709b17cb54fbc8cd1c0e732f54aa994628ad";

const api = axios.create({
	headers: {
		"Content-Type": "application/json",
		Accept: "application/json"
	},
	baseURL: host
});

export function getWalletAddress() {
	return new Promise((resolve, reject) => {
		const listenerTimeout = setTimeout(() => {
			window.removeEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
			reject("timeout");
		}, 10000);
		window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
		window.dispatchEvent(
			new CustomEvent("ICONEX_RELAY_REQUEST", {
				detail: {
					type: "REQUEST_ADDRESS"
				}
			})
		);
		function eventHandler(event) {
			const { type, payload } = event.detail;
			if (type === "RESPONSE_ADDRESS") {
				window.removeEventListener(
					"ICONEX_RELAY_RESPONSE",
					eventHandler,
					false
				);
				clearTimeout(listenerTimeout);
				resolve(payload);
			}
		}
	});
}
export function sendTransaction(params) {
	return new Promise((resolve, reject) => {
		const listenerTimeout = setTimeout(() => {
			window.removeEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
			reject("timeout");
		}, 100000);
		window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
		window.dispatchEvent(
			new CustomEvent("ICONEX_RELAY_REQUEST", {
				detail: {
					type: "REQUEST_JSON-RPC",
					payload: {
						jsonrpc: "2.0",
						method: "icx_sendTransaction",
						params: params,
						id: 1
					}
				}
			})
		);
		function eventHandler(event) {
			const { type, payload } = event.detail;
			if (type === "RESPONSE_JSON-RPC") {
				window.removeEventListener(
					"ICONEX_RELAY_RESPONSE",
					eventHandler,
					false
				);
				clearTimeout(listenerTimeout);
				resolve(payload);
			}
		}
	});
}

export function readyToBet(address) {
	return api
		.get(`dice/${scoreAddress}/player/${address}/houseSeed`)
		.then(res => {
			return res;
		});
}

export function roll(payload) {
	const { index, params } = payload;
	return api.post(`dice/${scoreAddress}/roll/${index}`, params).then(res => {
		return res;
	});
}
