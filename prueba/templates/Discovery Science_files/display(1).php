(function() {

function inIframe() {
    try {
        return (window.self !== window.top) ? 1 : 0;
    }
    catch (e) {
        return 1;
    }
}
function ReopenUrlBuilder(baseUrl) {

    this.baseUrl = baseUrl;

    /**
     * Get value of content attribute of meta tag with name attribute = name
     * Fallback to top if possible
     *
     * @return string
     */
    this._getMetaContent = function (name) {
        try {
            var meta = window.top.document.getElementsByTagName('meta');
            for (var i = 0; i < meta.length; i++) {
                if (meta[i].hasAttribute('name') && meta[i].getAttribute('name').toLowerCase() === name) {
                    var info = meta[i].getAttribute('content');
                    var indexToCut = Math.max(info.indexOf(' ', 256), info.indexOf(',', 256));
                    if (indexToCut > 384 || indexToCut < 20) {
                        indexToCut = 256;
                    }
                    return info.substring(0, indexToCut);
                }
            }
        } catch (e) {
        }

        return '';
    };

    this._getWidth = function () {
        return window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    };

    this._getHeight = function () {
        return window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
    };

    this._getTitle = function () {
        var title = document.title;

        if (inIframe()) {
            try {
                title = window.top.document.title;
            }
            catch (e) {
                title = '';
            }
        }

        return title;
    };

    this.build = function () {
        return this.baseUrl
            + '&cbrandom=' + Math.random()
            + '&cbtitle=' + encodeURIComponent(this._getTitle())
            + '&cbiframe=' + inIframe()
            + '&cbWidth=' + this._getWidth()
            + '&cbHeight=' + this._getHeight()
            + '&cbdescription=' + encodeURIComponent(this._getMetaContent('description'))
            + '&cbkeywords=' + encodeURIComponent(this._getMetaContent('keywords'))
    };
}
/**
 * Detect the browser
 *
 * Parse the passed user agent if possible so we can descide what we are going to do.
 *
 * @return Object The browser that has been detected.
 */
var browser = (function (n) {
    // var n = 'Dalvik/1.6.0 (Linux; U; Android 4.3; GT-I9300 Build/JSS15J)'.toLowerCase();
    n = n.replace('OPR', 'opera').toLowerCase();
    var b = {
        webkit: /webkit/.test(n),
        chrome: /chrome|crios/.test(n),
        safari: (/safari/.test(n) && !(/chrome/.test(n)) && !(/opios/.test(n))),
        mozilla: (/mozilla/.test(n)) && (!/(compatible|webkit)/.test(n)),
        firefox: /firefox/.test(n),
        msie: (/msie/.test(n)) && (!/opera/.test(n)),
        msedge: (/edge/.test(n)),
        ms_mobile: /iemobile/.test(n),
        opera: /opera/.test(n),
        // opios is Opera Mini in iOS
        opera_mini: (/opera mini/.test(n) || /opios/.test(n)),
        android: /android/.test(n),
        mac: /macintosh/.test(n),
        blackberry: /blackberry/.test(n),
        ios: /ipad|ipod|iphone/.test(n),
        // FaceBook userAgent
        fb: /fban\/fbios|fbav|fbios|fb_iab\/fb4a/.test(n),
        presto: /presto/.test(n),
        ieQuirksMode: (typeof document.compatMode !== 'undefined') ? document.compatMode !== 'CSS1Compat' && (/msie/.test(n)) && (!/opera/.test(n)) : false,
        ucbrowser: /UCBrowser|UCWEB/.test(n)
    };
    b.user_agent = n;

    // Check for the flash support
    b.flash_support = false;
    try {
        b.flash_support = navigator.mimeTypes['application/x-shockwave-flash'];
    }
    catch (e) {
    }

    // Get the browser version
    b.version = (b.safari) ? (n.match(/.+(?:ri)[\/: ]([\d.]+)/) || [])[1] : (n.match(/.+(?:ox|me|ra|ie)[\/: ]([\d.]+)/) || [])[1];

    b.touchable = 'ontouchstart' in document.documentElement;

    // Get the major browser version, like Chrome 41 or Firefox 38, from the full version
    b.major_version = parseInt(b.version);

    /* Detect if the current browser is a mobile browser or not. */
    b.is_mobile = b.android || b.ios || b.blackberry || b.ms_mobile || b.opera_mini || b.ucbrowser;

    return b;
})(navigator.userAgent);

var builder = new ReopenUrlBuilder("http:\/\/www.adnetworkperformance.com\/a\/display.php?r=293377&treqn=584900613&runauction=1&crr=5d8f72858c9eef7d4d59,,AYmtGYsZmdow3dgNnamZHbhN0NggGcshGY3V3Q3ACaqZ2K2xWckdnYzFHcqx3Q3AyQ3ACR2ASdxFXb7e851c100d7a0fee6c92");
var url = builder.build();

    (function(document, scriptElement, firstScript) {

    
    scriptElement = document.createElement('script');
    scriptCFASync = document.createAttribute("data-cfasync");
    scriptCFASync.value = false;
    scriptElement.setAttributeNode(scriptCFASync);

    scriptElement.src = url;
    var firstScript;
    if (typeof document.scripts !== 'undefined') {
        firstScript = document.scripts[0];
    }
    if (typeof firstScript == 'undefined') {
        firstScript = document.getElementsByTagName('script')[0];
    }
    firstScript.parentNode.insertBefore(scriptElement, firstScript);
        }(document));
})();
