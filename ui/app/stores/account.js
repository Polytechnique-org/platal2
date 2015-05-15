'use strict';

/** AccountStore: stores Account-related data.
 */

var Reflux = require('reflux');
var AccountActions = require('../actions.js');

/** Account fetcher
 *
 * TODO: Replace with an actual Ajax call.
 */
var loadAccount = function() {
  var accountData = {username: 'xelnor', name: "Xelnor"};
  window.setTimeout(
    function() {
      AccountActions.fetchAccount(accountData);
    },
    750
  );
}

var accountStore = Reflux.createStore({
  listenables: AccountActions,

  init: function() {
    // On startup, initiate a loadAccount event.
    loadAccount();
  },

  getInitialState: function() {
    this.account = {username: '', name: "(fetching...)"};
    return this.account;
  },

  onFetchAccount: function(account) {
    this.account = account;
    this.trigger(this.account);
  }
});

module.exports = accountStore;
