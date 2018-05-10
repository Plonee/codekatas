import { test } from 'tape';
import { Anagram } from './anagram';


test('should get the name right', t => {
  const anagram = new Anagram('oh, hi Mark')
  const expected = 'oh, hi Mark'
  t.equal(anagram.innerText, expected)
  t.end()
})


test('should innerTexts equal', t => {
  const anagram = new Anagram('oh, hi Mark')
  const anagramCopy = new Anagram('oh, hi Mark')
  t.equal(anagram.innerText, anagramCopy.innerText)
  t.end()
})
