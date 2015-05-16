'use strict';

/** AccountStore: stores Account-related data.
 */

var Reflux = require('reflux');
var request = require('superagent');

var AccountActions = require('../actions.js');

/** Account fetcher
 *
 * TODO: Replace with an actual Ajax call.
 */
var loadAccount = function() {
  request
    .get('http://platal2-demo.polytechnique.org/api/accounts/me')
    .set('Accept', 'application/json')
    .withCredentials()
    .end(function(err, res) {
      if (res && res.ok) {
        AccountActions.fetchAccount({username: res.body.hruid, name: res.body.full_name, loading: false});
      } else {
        AccountActions.fetchAccount({username: '', name: "" + err, loading: false});
      }
    });
}

var accountStore = Reflux.createStore({
  listenables: AccountActions,

  init: function() {
    // On startup, initiate a loadAccount event.
    loadAccount();
  },

  getInitialState: function() {
    this.account = {username: '', name: '', loading: true};
    return this.account;
  },

  onFetchAccount: function(account) {
    this.account = account;
    this.trigger(this.account);
  }
});

module.exports = accountStore;
