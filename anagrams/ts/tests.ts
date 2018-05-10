import { test } from 'tape';
import { Anagram } from './anagram';


test('should get the name right', t => {
  const anagram = new Anagram('hi')
  const expected = 'hi'
  t.equal(anagram.innerText, expected)
  t.end()
})
