def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))
def find_palindromes(str_list):
    return [s for s in str_list if s == s[::-1]]
def sieve_of_eratosthenes(num_list):
    primes = []
    for num in num_list:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
def anagrams(word, word_list):
    sorted_word = sorted(word.lower().replace(' ', ''))
    return [w for w in word_list if sorted(w.lower().replace(' ', '')) == sorted_word and w.lower() != word.lower()]