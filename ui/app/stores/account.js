'use strict';

/** AccountStore: stores Account-related data.
 */

var Reflux = require('reflux');
var request = require('superagent-bluebird-promise');

var AccountActions = require('../actions.js');

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
    request
      .get('http://platal2-demo.polytechnique.org/api/accounts/me')
      .set('Accept', 'application/json')
      .withCredentials()
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
