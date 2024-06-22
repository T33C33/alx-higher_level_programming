#!/usr/bin/node
exports.callMeMoby = function (x, extFunc) {
    for (let i = 0; i < x; i++) {
        extFunc();
    }
};
