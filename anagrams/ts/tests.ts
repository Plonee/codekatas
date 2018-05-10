import { test } from 'tape';
import { Anagram } from './anagram';


test('should get the name right', t => {
  const anagram = new Anagram('oh, hi Mark')
  const expected = 'oh, hi Mark'
  t.equal(anagram.innerText, expected)
  t.end()
})
