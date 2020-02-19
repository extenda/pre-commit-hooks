const { rules } = require('./index.js');

const tense = rules['imperative-tense'];

describe('Imperative-tense', () => {
    test('It rejects past tense', () => {
        expect(tense({subject: 'feat: added new feature'})).toEqual(expect.arrayContaining([ false ]));
    });

    test('It rejects present tense', () => {
        expect(tense({subject: 'feat: adds new feature'})).toEqual(expect.arrayContaining([ false ]));
    });

    test('It accepts imperative tense', () => {
        expect(tense({subject: 'feat: add new feature'})).toEqual(expect.arrayContaining([ true ]));
    });

    test('It accepts missing subject', () => {
       expect(tense({})).toEqual([true]);
    });
});
