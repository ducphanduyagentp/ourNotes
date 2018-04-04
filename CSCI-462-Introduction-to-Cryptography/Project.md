# Project

* Implement symmetric-key algorthm
* Based on a special family of graph
* Multivariate cryptography
* Vertices => vectors
* Vertices have color
* Message are represented by vertex
* Password is sequence of color => How to traverse the graph
* Encrypt and decrypt text files (+3 credit if for any data)
* Attack on letter frequences
* For 6 and 7, plot the results on graphs

## Example

- K = (A, t = (t_1, t_2, ..., t_s), A**(-1))
  - t is the password
- M = (m_1, ..., m_n)

1. M x A = MM
2. Central map
  - F(MM) = CC
3. C = CC x A**(-1)

p = 29
t = (2, 3, 11)
MM = (22,0,0,12,8) ==> n = 5
1. N_(t_i) (MM) = [22 + t_i, *, *, *, *] = L
2. N_2(MM) = [24, L_2, L_3, L_4, L_5] (L from p: lines from points)
3. L_2 = p_2 + p_1 * L_1
...
4. N_3([24, 6, 16, 12, 8]) = [24 + 3, *, *, *, *] (points from lines)
= (27, 25, 28, 21, 3)
5. N_11((27, 25, 28, 21, 3)) = [(27+11) mod 29, ...]
==> CC = [9, 7 14, 14, 23]