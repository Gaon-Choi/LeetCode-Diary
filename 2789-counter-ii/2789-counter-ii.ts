type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let cnt: number = init;
    const initial_value: number = init;

    return {
      increment: () => {
        cnt++;
        return cnt;
      },
      decrement: () => {
        cnt--;
        return cnt;
      },
      reset: () => {
        cnt = initial_value;
        return cnt;
      }
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */