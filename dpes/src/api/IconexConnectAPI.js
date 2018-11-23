const getAddress = () => new Promise((resolve) => {
  const eventHandler = (event) => {
    const { type, payload } = event.detail;
    if (type === 'RESPONSE_ADDRESS') {
      resolve(payload);
    }
    window.removeEventListener('ICONEX_RELAY_RESPONSE', eventHandler);
  };
  window.addEventListener('ICONEX_RELAY_RESPONSE', eventHandler);
  window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
    detail: {
      type: 'REQUEST_ADDRESS',
    },
  }));
});


const sendTransaction = params => new Promise((resolve) => {
  const eventHandler = (event) => {
    const { type, payload } = event.detail;
    if (type === 'RESPONSE_JSON-RPC') {
      resolve(payload.result);
    }
    window.removeEventListener('ICONEX_RELAY_RESPONSE', eventHandler);
  };
  window.addEventListener('ICONEX_RELAY_RESPONSE', eventHandler);
  window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
    detail: {
      type: 'REQUEST_JSON-RPC',
      payload: params,
    },
  }));
});

export default {
  getAddress,
  sendTransaction,
};
