const TIMEOUT = 10000

export function requestAddress(timeout) {
    return new Promise((resolve, reject) => {
        const listenerTimeout = setTimeout(()=>{
            window.removeEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
            reject('timeout')
        }, timeout || TIMEOUT)
        window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
        window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
            detail: {
                type: 'REQUEST_ADDRESS'
            }
        }))
        function eventHandler(event) {
            const { type, payload } = event.detail
            if (type === 'RESPONSE_ADDRESS') {
                window.removeEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
                clearTimeout(listenerTimeout)
                resolve(payload)
            }
        }
    })
}

// TODO 
// timeout 지정하지 않는 경우
export function requestJsonRpc(rawTransaction, timeout) {
    return new Promise((resolve, reject) => {
        const listenerTimeout = setTimeout(()=>{
            window.removeEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
            reject('timeout')
        }, timeout || TIMEOUT)
        window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
        window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
            detail: {
                type: 'REQUEST_JSON-RPC',
                payload: {
                    "jsonrpc": "2.0",
                    "method": "icx_sendTransaction",
                    "params": rawTransaction,
                    "id": 50889
                }
            }
        }))
        function eventHandler(event) {
            const { type, payload } = event.detail
            if (type === 'RESPONSE_JSON-RPC') {
                window.removeEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
                clearTimeout(listenerTimeout)
                resolve(payload)
            }
        }
    })
}