module.exports = {
  extends: [
    '@commitlint/config-conventional',
  ],
  plugins: [
    'tense',
  ],
  rules: {
    'scope-case': [0, 'always', 'lower-case'],
    'imperative-tense': [2, 'always'],
  }
};
