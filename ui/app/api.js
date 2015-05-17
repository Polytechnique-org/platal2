'use strict';


/** Wrapper for platal2 API calls.
 *
 * Handles common options and setup.
 *
 *
 * Usage:
 *
 * var PlatalAPI = require('./api.js')
 * PlatalAPI
 *   .get('sub/url/').then(function(res) {
 *     // do something with the reply
 *   }, function(error) {
 *     // do something with the error
 *   });
 *
 *
 * The PlatalAPI *MUST* be initialized first; this is the task of the application entrypoint.
 * Call:
 *
 * var PlatalAPI = require('./api.js')
 * PlatalAPI.configure({rootUrl: 'http://platal2-demo.polytechnique.org/api/'});
 */

var request = require('superagent-bluebird-promise');

function APIWrapper() {
  this.rootUrl = null;
}

APIWrapper.prototype.configure = function(options) {
  this.rootUrl = options.rootUrl || this.rootUrl;
};

APIWrapper.prototype.get = function(url) {
  var fullUrl = this.rootUrl + url;
  return request
    .get(fullUrl)
    .set('Accept', 'application/json')
    .withCredentials();
};

var PlatalAPI = new APIWrapper();

module.exports = PlatalAPI;
