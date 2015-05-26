'use strict';

/** AccountStore: stores Account-related data.
 */

var Reflux = require('reflux');

var AccountActions = require('../actions.js').AccountActions;
var PlatalAPI = require('../api.js');

var accountStore = Reflux.createStore({
  listenables: AccountActions,

  init: function() {
    // On startup, initiate a loadAccount event.
    AccountActions.fetchAccount();
  },

  getInitialState: function() {
    this.account = {username: '', name: '', loading: true};
    return this.account;
  },

  onFetchAccount: function() {
    PlatalAPI.get('accounts/me')
      .then(function(res) {
          AccountActions.fetchAccount.completed({error: null, username: res.body.hruid, name: res.body.full_name, loading: false});
        }, function(error) {
          AccountActions.fetchAccount.failed({error: error, loading: false});
        }
      );
  },

  onFetchAccountCompleted: function(account) {
    this.account = account;
    this.trigger(this.account);
  },

  onFetchAccountFailed: function(account) {
    this.account = account;
    this.trigger(this.account);
  }
});

module.exports = accountStore;
