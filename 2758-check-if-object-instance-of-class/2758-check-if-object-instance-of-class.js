/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined || typeof classFunction !== 'function') {
        return false
    }

    // inheritance -> prototype chain
    let protoType = Object.getPrototypeOf(obj);

    // iterate the prototype chain of the given object
    while (protoType != null) {
        if (protoType === classFunction.prototype) {
            return true;
        }

        // traverse deeper
        protoType = Object.getPrototypeOf(protoType)
    }

    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */