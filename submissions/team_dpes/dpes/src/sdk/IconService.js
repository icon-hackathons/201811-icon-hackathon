import IconService, {
  HttpProvider,
} from 'icon-sdk-js';
import Constants from '../constants';

class Provider {
  constructor() {
    // HttpProvider is used to communicate with http.
    this.provider = new HttpProvider(Constants.PROVIDER_URL);
    // Create IconService instance
    this.iconService = new IconService(this.provider);
  }
}

const provider = new Provider();
const { iconService } = provider;

export default iconService;
