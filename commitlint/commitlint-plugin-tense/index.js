const fs = require('fs');
const path = require('path');

// Imperative mode blacklist.
// From https://github.com/tommarshall/git-good-commit
const blacklist = fs.readFileSync(path.join(__dirname, 'blacklist.txt'), 'utf8')
    .split(/\W+/)
    .map((word) => word.trim())
    .filter((word) => word.length > 0);

module.exports = {
    rules: {
        'imperative-tense': (parsed, when) => {
            const { subject } = parsed;
            if (!subject) {
                return [true];
            }
            const success = blacklist.every((word) => !subject.includes(word));
            return [success, "Use the imperative mood in the subject, e.g 'fix' not 'fixes'"];
        }
    }
};
