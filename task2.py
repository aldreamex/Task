def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    m_M_one = given_mass1 / molar_mass1
    m_M_two = given_mass2 / molar_mass2
    summ_n_M_all = m_M_one + m_M_two
    P = 0.082
    T_k = temp + 273.15
    chislitel = summ_n_M_all * P * T_k

    P_total = chislitel / volume

    return P_total

# summ = solution(44, 30, 3, 2, 5, 50)
print (solution(44, 30, 3, 2, 5, 50))