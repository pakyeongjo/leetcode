class IsIsomorphic:
    def solution(self, s, t):
        a = list(zip(s, t))
        hash_s, hash_t = {}, {}
        format_s, format_t = "", ""
        value = 0
        for obj in a:
            if not hash_s.get(obj[0]) and not hash_t.get(obj[1]):
                value += 1
                hash_s[obj[0]], hash_t[obj[1]] = value, value
                format_s += str(value)
                format_t += str(value)
            elif hash_s.get(obj[0]) and hash_t.get(obj[1]):
                format_s += str(hash_s[obj[0]])
                format_t += str(hash_t[obj[1]])
            else:
                return False
            if format_s != format_t:
                return False
            # if hash_s.get(obj[0]):
            #     format_s += str(hash_s[obj[0]])
            # else:
            #     value += 1
            #     hash_s[obj[0]] = value
            #     format_s += str(value)

        # return hash_s, hash_t

        return format_s, format_t

    def solution1(self, s, t):
        format_s = ""
        hashmap = {}
        value = 0
        for letter in s:
            if hashmap.get(letter):
                format_s += str(hashmap[letter])
            else:
                value += 1
                hashmap[letter] = value
                format_s += str(value)

        format_t = ""
        hashmap = {}
        value = 0
        for letter in t:
            if hashmap.get(letter):
                format_t += str(hashmap[letter])
            else:
                value += 1
                hashmap[letter] = value
                format_t += str(value)
            if format_s[:len(format_t)] != format_t:
                return format_s, format_t, value
        # return hashmap
        # return format_t
        return format_s, format_t
