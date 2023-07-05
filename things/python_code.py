ADD_1_TO_A_GIVEN_NUMBER | def addOne ( x ) :
    m = 1
    while ( x & m ) :
        x = x ^ m
        m <<= 1
    x = x ^ m
    return x

ADD_1_TO_A_GIVEN_NUMBER_1 | def addOne ( x ) :
    return ( - ( ~ x ) )

ANALYSIS_OF_ALGORITHMS_SET_2_ASYMPTOTIC_ANALYSIS | def search ( arr , n , x ) :
    i = 0
    for i in range ( i , n ) :
        if ( arr [ i ] == x ) :
            return i
    return - 1

AREA_OF_THE_CIRCLE_THAT_HAS_A_SQUARE_AND_A_CIRCLE_INSCRIBED_IN_IT | def getArea ( a ) :
    area = ( math.pi * a * a ) / 4
    return area

AREA_SQUARE_CIRCUMSCRIBED_CIRCLE | def find_Area ( r ) :
    return ( 2 * r * r )

ARRAY_ELEMENT_MOVED_K_USING_SINGLE_MOVES | def winner ( a , n , k ) :
    if k >= n - 1 :
        return n
    best = 0
    times = 0
    for i in range ( n ) :
        if a [ i ] > best :
            best = a [ i ]
            if i == True :
                times = 1
        else :
            times += 1
        if times >= k :
            return best
    return best

ARRAY_RANGE_QUERIES_ELEMENTS_FREQUENCY_VALUE | def solveQuery ( start , end , arr ) :
    frequency = dict ( )
    for i in range ( start , end + 1 ) :
        if arr [ i ] in frequency.keys ( ) :
            frequency [ arr [ i ] ] += 1
        else :
            frequency [ arr [ i ] ] = 1
    count = 0
    for x in frequency :
        if x == frequency [ x ] :
            count += 1
    return count

BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS | def gcd ( a , b ) :
    if a == 0 :
        return b
    return gcd ( b % a , a )

BINARY_SEARCH | def binarySearch ( arr , l , r , x ) :
    if r >= l :
        mid = l + ( r - l ) // 2
        if arr [ mid ] == x :
            return mid
        elif arr [ mid ] > x :
            return binarySearch ( arr , l , mid - 1 , x )
        else :
            return binarySearch ( arr , mid + 1 , r , x )
    else :
        return - 1

BREAK_NUMBER_THREE_PARTS | def count_of_ways ( n ) :
    count = 0
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , n + 1 ) :
            for k in range ( 0 , n + 1 ) :
                if ( i + j + k == n ) :
                    count = count + 1
    return count

BREAK_NUMBER_THREE_PARTS_1 | def count_of_ways ( n ) :
    count = 0
    count = ( n + 1 ) * ( n + 2 ) // 2
    return count

CAESAR_CIPHER | def encrypt ( text , s ) :
    result = ""
    for i in range ( len ( text ) ) :
        char = text [ i ]
        if ( char.isupper ( ) ) :
            result += chr ( ( ord ( char ) + s - 65 ) % 26 + 65 )
        else :
            result += chr ( ( ord ( char ) + s - 97 ) % 26 + 97 )
    return result

CALCULATE_ANGLE_HOUR_HAND_MINUTE_HAND | def calcAngle ( h , m ) :
    if ( h < 0 or m < 0 or h > 12 or m > 60 ) :
        print ( 'Wrong input' )
    if ( h == 12 ) :
        h = 0
    if ( m == 60 ) :
        m = 0
    hour_angle = int ( 0.5 * ( h * 60 + m ) )
    minute_angle = int ( 6 * m )
    angle = abs ( hour_angle - minute_angle )
    angle = min ( 360 - angle , angle )
    return angle

CALCULATE_MAXIMUM_VALUE_USING_SIGN_TWO_NUMBERS_STRING | def calcMaxValue ( str ) :
    res = ord ( str [ 0 ] ) - 48
    for i in range ( 1 , len ( str ) ) :
        if ( str [ i ] == '0' or str [ i ] == '1' or res < 2 ) :
            res += ord ( str [ i ] ) - 48
        else :
            res += ord ( str [ i ] ) - 48
    return res

CALCULATE_SUM_OF_ALL_NUMBERS_PRESENT_IN_A_STRING | def findSum ( str ) :
    temp = "0"
    Sum = 0
    for ch in str :
        if ( ch.isdigit ( ) ) :
            temp += ch
        else :
            Sum += int ( temp )
            temp = "0"
    return Sum + int ( temp )

CALCULATE_VOLUME_DODECAHEDRON | def vol_of_dodecahedron ( side ) :
    return ( ( ( 15 + ( 7 * ( math.sqrt ( 5 ) ) ) ) / 4 ) * ( math.pow ( side , 3 ) ) )

CASSINIS_IDENTITY | def cassini ( n ) :
    return - 1 if ( n & 1 ) else 1

CEILING_IN_A_SORTED_ARRAY_1 | def ceilSearch ( arr , low , high , x ) :
    if x <= arr [ low ] :
        return low
    if x > arr [ high ] :
        return - 1
    mid = ( low + high ) / 2
    if arr [ mid ] == x :
        return mid
    elif arr [ mid ] < x :
        if mid + 1 <= high and x <= arr [ mid + 1 ] :
            return mid + 1
        else :
            return ceilSearch ( arr , mid + 1 , high , x )
    else :
        if mid - 1 >= low and x > arr [ mid - 1 ] :
            return mid
        else :
            return ceilSearch ( arr , low , mid - 1 , x )

CENTER_ELEMENT_OF_MATRIX_EQUALS_SUMS_OF_HALF_DIAGONALS | def HalfDiagonalSums ( mat , n ) :
    diag1_left = 0
    diag1_right = 0
    diag2_left = 0
    diag2_right = 0
    i = 0
    j = n - 1
    while i < n :
        if ( i < n // 2 ) :
            diag1_left += mat [ i ] [ i ]
            diag2_left += mat [ j ] [ i ]
        elif ( i > n // 2 ) :
            diag1_right += mat [ i ] [ i ]
            diag2_right += mat [ j ] [ i ]
        i += 1
        j -= 1
    return ( diag1_left == diag2_right and diag2_right == diag2_left and diag1_right == diag2_left and diag2_right == mat [ n // 2 ] [ n // 2 ] )

CHANGE_BITS_CAN_MADE_ONE_FLIP | def canMakeAllSame ( str ) :
    zeros = 0
    ones = 0
    for i in range ( 0 , len ( str ) ) :
        ch = str [ i ]
        if ( ch == '0' ) :
            zeros = zeros + 1
        else :
            ones = ones + 1
    return ( zeros == 1 or ones == 1 )

CHANGE_BITS_CAN_MADE_ONE_FLIP_1 | def isOneFlip ( str ) :
    sum = 0
    n = len ( str )
    for i in range ( 0 , n ) :
        sum += ord ( str [ i ] ) - ord ( '0' )
    return ( sum == n - 1 or sum == 1 )

CHECK_ARRAY_MAJORITY_ELEMENT | def isMajority ( a, n ) :
    mp = { }
    for i in range(n) :
        if a[i] in mp : mp [ a[i] ] += 1
        else : mp [ a[i] ] = 1
    for x in mp :
        if mp [ x ] >= len ( a ) // 2 :
            return True
    return False

CHECK_ARRAY_REPRESENTS_INORDER_BINARY_SEARCH_TREE_NOT | def isInorder ( arr , n ) :
    if ( n == 0 or n == 1 ) :
        return True
    for i in range ( 1 , n , 1 ) :
        if ( arr [ i - 1 ] > arr [ i ] ) :
            return False
    return True

CHECK_DIVISIBILITY_BINARY_STRING_2K | def isDivisible ( str , k ) :
    n = len ( str )
    c = 0
    for i in range ( 0 , k ) :
        if ( str [ n - i - 1 ] == '0' ) :
            c += 1
    return ( c == k )

CHECK_DIVISIBILITY_LARGE_NUMBER_999 | def isDivisible999 ( num ) :
    n = len ( num )
    if ( n == 0 and num [ 0 ] == '0' ) :
        return True
    if ( ( n % 3 ) == 1 ) :
        num = "00" + num
    if ( ( n % 3 ) == 2 ) :
        num = "0" + num
    gSum = 0
    for i in range ( 0 , n , 3 ) :
        group = 0
        group += ( ord ( num [ i ] ) - 48 ) * 100
        group += ( ord ( num [ i + 1 ] ) - 48 ) * 10
        group += ( ord ( num [ i + 2 ] ) - 48 )
        gSum += group
    if ( gSum > 1000 ) :
        num = str ( gSum )
        n = len ( num )
        gSum = isDivisible999 ( num )
    return ( gSum == 999 )

CHECK_GIVEN_CIRCLE_LIES_COMPLETELY_INSIDE_RING_FORMED_TWO_CONCENTRIC_CIRCLES | def checkcircle ( r , R , r1 , x1 , y1 ) :
    dis = int ( math.sqrt ( x1 * x1 + y1 * y1 ) )
    return ( dis - r1 >= R and dis + r1 <= r )

CHECK_GIVEN_STRING_CAN_SPLIT_FOUR_DISTINCT_STRINGS | def check ( s ) :
    if ( len ( s ) >= 10 ) :
        return True
    for i in range ( 1 , len ( s ) ) :
        for j in range ( i + 1 , len ( s ) ) :
            for k in range ( j + 1 , len ( s ) ) :
                s1 = s [ 0 : i ]
                s2 = s [ i : j ]
                s3 = s [ j : k ]
                s4 = s [ k : len ( s ) ]
                if ( s1 != s2 and s1 != s3 and s1 != s4 and s2 != s3 and s2 != s4 and s3 != s4 ) :
                    return True
    return False

CHECK_GIVEN_STRING_ROTATION_PALINDROME | def isPalindrome ( string ) :
    l = 0
    h = len ( string ) - 1
    while h > l :
        l += 1
        h -= 1
        if string [ l - 1 ] != string [ h + 1 ] :
            return False
    return True

CHECK_IF_ALL_THE_ELEMENTS_CAN_BE_MADE_OF_SAME_PARITY_BY_INVERTING_ADJACENT_ELEMENTS | def flipsPossible ( a , n ) :
    count_odd = 0
    count_even = 0
    for i in range ( n ) :
        if ( a [ i ] & 1 ) :
            count_odd += 1
        else :
            count_even += 1
    if ( count_odd % 2 and count_even % 2 ) :
        return False
    else :
        return True

CHECK_IF_ARRAY_ELEMENTS_ARE_CONSECUTIVE | def areConsecutive ( arr , n ) :
    if ( n < 1 ) :
        return False
    Min = min ( arr )
    Max = max ( arr )
    if ( Max - Min + 1 == n ) :
        visited = [ False for i in range ( n ) ]
        for i in range ( n ) :
            if ( visited [ arr [ i ] - Min ] != False ) :
                return False
            visited [ arr [ i ] - Min ] = True
        return True
    return False

CHECK_IF_A_GIVEN_ARRAY_CAN_REPRESENT_PREORDER_TRAVERSAL_OF_BINARY_SEARCH_TREE | def canRepresentBST ( pre, n ) :
    s = [ ]
    root = -2147483648
    for i in range(n) :
        if pre[i] < root :
            return False
        while ( len ( s ) > 0 and s [ - 1 ] < pre[i] ) :
            root = s.pop ( )
        s.append ( pre[i] )
    return True

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER | def isPower ( x , y ) :
    if ( x == 1 ) :
        return ( y == 1 )
    pow = 1
    while ( pow < y ) :
        pow = pow * x
    return ( pow == y )

CHECK_IF_A_NUMBER_IS_POWER_OF_ANOTHER_NUMBER_1 | def isPower ( x , y ) :
    res1 = int ( math.log ( y ) / math.log ( x ) )
    res2 = math.log ( y ) / math.log ( x )
    return 1 if ( res1 == res2 ) else 0

CHECK_IF_STRING_REMAINS_PALINDROME_AFTER_REMOVING_GIVEN_NUMBER_OF_CHARACTERS | def isPossible ( str , n ) :
    l = len ( str )
    if ( l >= n ) :
        return True
    return False

CHECK_IF_X_CAN_GIVE_CHANGE_TO_EVERY_PERSON_IN_THE_QUEUE | def isChangeable ( notes , n ) :
    fiveCount = 0
    tenCount = 0
    for i in range ( n ) :
        if ( notes [ i ] == 5 ) :
            fiveCount += 1
        elif ( notes [ i ] == 10 ) :
            if ( fiveCount > 0 ) :
                fiveCount -= 1
                tenCount += 1
            else :
                return 0
        else :
            if ( fiveCount > 0 and tenCount > 0 ) :
                fiveCount -= 1
                tenCount -= 1
            elif ( fiveCount >= 3 ) :
                fiveCount -= 3
            else :
                return 0
    return 1

CHECK_INTEGER_OVERFLOW_MULTIPLICATION | def isOverflow ( a , b ) :
    if ( a == 0 or b == 0 ) :
        return False
    result = a * b
    if ( result >= 9223372036854775807 or result <= - 9223372036854775808 ) :
        result = 0
    if ( a == ( result // b ) ) :
        return False
    else :
        return True

CHECK_LARGE_NUMBER_DIVISIBLE_11_NOT | def check ( str ) :
    n = len ( str )
    oddDigSum = 0
    evenDigSum = 0
    for i in range ( 0 , n ) :
        if ( i % 2 == 0 ) :
            oddDigSum = oddDigSum + ( ord ( str [ i ] ) - 48 )
        else :
            evenDigSum = evenDigSum + ( ord ( str [ i ] ) - 48 )
    return ( ( oddDigSum - evenDigSum ) % 11 == 0 )

CHECK_LARGE_NUMBER_DIVISIBLE_13_NOT | def checkDivisibility ( num ) :
    length = len ( num )
    if ( length == 1 and num [ 0 ] == '0' ) :
        return True
    if ( length % 3 == 1 ) :
        num = str ( num ) + "00"
        length += 2
    elif ( length % 3 == 2 ) :
        num = str ( num ) + "0"
        length += 1
    sum = 0
    p = 1
    for i in range ( length - 1 , - 1 , - 3 ) :
        group = 0
        group += ord ( num [ i ] ) - ord ( '0' )
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 10
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 100
        sum = sum + group * p
        p *= ( - 1 )
    sum = abs ( sum )
    return ( sum % 13 == 0 )

CHECK_LARGE_NUMBER_DIVISIBLE_4_NOT | def check ( str ) :
    n = len ( str )
    if ( n == 0 ) :
        return False
    if ( n == 1 ) :
        return ( ( str [ 0 ] - '0' ) % 4 == 0 )
    last = ( int ) ( str [ n - 1 ] )
    second_last = ( int ) ( str [ n - 2 ] )
    return ( ( second_last * 10 + last ) % 4 == 0 )

CHECK_LARGE_NUMBER_DIVISIBLE_9_NOT | def check ( str ) :
    n = len ( str )
    digitSum = 0
    for i in range ( 0 , n ) :
        digitSum = digitSum + ord ( str [ i ] ) - 48
    return ( digitSum % 9 == 0 )

CHECK_NUMBER_IS_PERFECT_SQUARE_USING_ADDITIONSUBTRACTION | def isPerfectSquare ( n ) :
    i = 1
    the_sum = 0
    while the_sum < n :
        the_sum += i
        if the_sum == n :
            return True
        i += 2
    return False

CHECK_POSSIBLE_TRANSFORM_ONE_STRING_ANOTHER | def check ( s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    dp = ( [ [ False for i in range ( m + 1 ) ] for i in range ( n + 1 ) ] )
    dp [ 0 ] [ 0 ] = True
    for i in range ( len ( s1 ) ) :
        for j in range ( len ( s2 ) + 1 ) :
            if ( dp [ i ] [ j ] ) :
                if ( ( j < len ( s2 ) and ( s1 [ i ].upper ( ) == s2 [ j ] ) ) ) :
                    dp [ i + 1 ] [ j + 1 ] = True
                if ( s1 [ i ].isupper ( ) == False ) :
                    dp [ i + 1 ] [ j ] = True
    return ( dp [ n ] [ m ] )

CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED_1 | def checkReverse ( arr , n ) :
    if ( n == 1 ) :
        return True
    i = 1
    for i in range ( 1 , n ) :
        if arr [ i - 1 ] >= arr [ i ] :
            break
        else:
            if ( i == n ) :
                return True
    j = i
    i += 1
    while ( arr [ j ] < arr [ j - 1 ] ) :
        if ( i > 1 and arr [ j ] < arr [ i - 2 ] ) :
            return False
        j += 1
    if ( j == n ) :
        return True
    k = j
    if ( arr [ k ] < arr [ i - 1 ] ) :
        return False
    while ( k > 1 and k < n ) :
        if ( arr [ k ] < arr [ k - 1 ] ) :
            return False
        k += 1
    return True

CHECK_STRING_CAN_OBTAINED_ROTATING_ANOTHER_STRING_2_PLACES | def isRotated ( str1 , str2 ) :
    if ( len ( str1 ) != len ( str2 ) ) :
        return False
    clock_rot = ""
    anticlock_rot = ""
    l = len ( str2 )
    anticlock_rot = ( anticlock_rot + str2 [ l - 2 : ] + str2 [ 0 : l - 2 ] )
    clock_rot = clock_rot + str2 [ 2 : ] + str2 [ 0 : 2 ]
    return ( str1 == clock_rot or str1 == anticlock_rot )

CHECK_STRING_FOLLOWS_ANBN_PATTERN_NOT | def isAnBn ( s ) :
    n = len ( s )
    for i in range ( n ) :
        if ( s [ i ] != 'a' ) :
            break
    if ( i * 2 != n ) :
        return False
    for j in range ( i , n ) :
        if ( s [ j ] != 'b' ) :
            return False
    return True

CHECK_SUMS_TH_ROW_TH_COLUMN_MATRIX | def areSumSame ( a , n , m ) :
    sum1 = 0
    sum2 = 0
    for i in range ( 0 , n ) :
        sum1 = 0
        sum2 = 0
        for j in range ( 0 , m ) :
            sum1 += a [ i ] [ j ]
            sum2 += a [ j ] [ i ]
        if ( sum1 == sum2 ) :
            return 1
    return 0

CHECK_TWO_GIVEN_CIRCLES_TOUCH_INTERSECT | def circle ( x1 , y1 , x2 , y2 , r1 , r2 ) :
    distSq = ( x1 - x2 ) * ( x1 - x2 ) + ( y1 - y2 ) * ( y1 - y2 )
    radSumSq = ( r1 + r2 ) * ( r1 + r2 )
    if ( distSq == radSumSq ) :
        return 1
    elif ( distSq > radSumSq ) :
        return - 1
    else :
        return 0

CHECK_VALID_SEQUENCE_DIVISIBLE_M_1 | def isPossible ( n , index , modulo , M , arr , dp ) :
    modulo = ( ( modulo % M ) + M ) % M
    if ( index == n ) :
        if ( modulo == 0 ) :
            return 1
        return 0
    if ( dp [ index ] [ modulo ] != - 1 ) :
        return dp [ index ] [ modulo ]
    placeAdd = isPossible ( n , index + 1 , modulo + arr [ index ] , M , arr , dp )
    placeMinus = isPossible ( n , index + 1 , modulo - arr [ index ] , M , arr , dp )
    res = bool ( placeAdd or placeMinus )
    dp [ index ] [ modulo ] = res
    return res

CHECK_WHETHER_ARITHMETIC_PROGRESSION_CAN_FORMED_GIVEN_ARRAY | def checkIsAP ( arr , n ) :
    if ( n == 1 ) : return True
    arr.sort ( )
    d = arr [ 1 ] - arr [ 0 ]
    for i in range ( 2 , n ) :
        if ( arr [ i ] - arr [ i - 1 ] != d ) :
            return False
    return True

CHECK_WHETHER_GIVEN_DEGREES_VERTICES_REPRESENT_GRAPH_TREE | def check ( degree , n ) :
    deg_sum = 0
    for i in range(n):
        deg_sum += degree[i]
    if ( 2 * ( n - 1 ) == deg_sum ) :
        return True
    else :
        return False

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD | def isEven ( n ) :
    return ( n % 2 == 0 )

CHECK_WHETHER_GIVEN_NUMBER_EVEN_ODD_1 | def isEven ( n ) :
    return ( not ( n & 1 ) )

CHECK_WHETHER_LARGE_NUMBER_DIVISIBLE_7 | def isdivisible7 ( num ) :
    n = len ( num )
    if ( n == 0 and num [ 0 ] == '\n' ) :
        return 1
    if ( n % 3 == 1 ) :
        num = str ( num ) + "00"
        n += 2
    elif ( n % 3 == 2 ) :
        num = str ( num ) + "0"
        n += 1
    GSum = 0
    p = 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        group = 0
        group += ord ( num [ i ] ) - ord ( '0' )
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 10
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 100
        GSum = GSum + group * p
        p *= ( - 1 )
    return ( GSum % 7 == 0 )

CHECK_WHETHER_TRIANGLE_VALID_NOT_SIDES_GIVEN | def checkValidity ( a , b , c ) :
    if ( a + b <= c ) or ( a + c <= b ) or ( b + c <= a ) :
        return False
    else :
        return True

CIRCULAR_MATRIX_CONSTRUCT_A_MATRIX_WITH_NUMBERS_1_TO_MN_IN_SPIRAL_WAY | def spiralFill ( m , n , a ) :
    val = 1
    k , l = 0 , 0
    while ( k < m and l < n ) :
        for i in range ( l , n ) :
            a [ k ] [ i ] = val
            val += 1
        k += 1
        for i in range ( k , m ) :
            a [ i ] [ n - 1 ] = val
            val += 1
        n -= 1
        if ( k < m ) :
            for i in range ( n - 1 , l - 1 , - 1 ) :
                a [ m - 1 ] [ i ] = val
                val += 1
            m -= 1
        if ( l < n ) :
            for i in range ( m - 1 , k - 1 , - 1 ) :
                a [ i ] [ l ] = val
                val += 1
            l += 1

COMPUTE_AVERAGE_TWO_NUMBERS_WITHOUT_OVERFLOW | def compute_average ( a , b ) :
    return floor ( ( a + b ) / 2 )

COMPUTE_MODULUS_DIVISION_BY_A_POWER_OF_2_NUMBER | def getModulo ( n , d ) :
    return ( n & ( d - 1 ) )

COMPUTE_NCR_P_SET_1_INTRODUCTION_AND_DYNAMIC_PROGRAMMING_SOLUTION | def nCrModp ( n , r , p ) :
    C = [ 0 for i in range ( r + 1 ) ]
    C [ 0 ] = 1
    for i in range ( 1 , n + 1 ) :
        for j in range ( min ( i , r ) , 0 , - 1 ) :
            C [ j ] = ( C [ j ] + C [ j - 1 ] ) % p
    return C [ r ]

CONSTRUCT_LEXICOGRAPHICALLY_SMALLEST_PALINDROME | def constructPalin ( string , l ) :
    string = list ( string )
    i = - 1
    j = l
    while i < j :
        i += 1
        j -= 1
        if ( string [ i ] == string [ j ] and string [ i ] != '*' ) :
            continue
        elif ( string [ i ] == string [ j ] and string [ i ] == '*' ) :
            string [ i ] = 'a'
            string [ j ] = 'a'
            continue
        elif string [ i ] == '*' :
            string [ i ] = string [ j ]
            continue
        elif string [ j ] == '*' :
            string [ j ] = string [ i ]
            continue
        print ( "Not Possible" )
        return ""
    return ''.join ( string )

CONVERT_DECIMAL_FRACTION_BINARY_NUMBER | def decimalToBinary ( num , k_prec ) :
    binary = ""
    Integral = int ( num )
    fractional = num - Integral
    while ( Integral > 0 ) :
        rem = Integral % 2
        binary += str ( rem )
        Integral //= 2
    binary = binary [ : : - 1 ]
    binary += '.'
    while ( k_prec > 0 ) :
        fractional *= 2
        fract_bit = int ( fractional )
        if ( fract_bit == 1 ) :
            fractional -= fract_bit
            binary += '1'
        else :
            binary += '0'
        k_prec -= 1
    return binary

CONVERT_STRICTLY_INCREASING_ARRAY_MINIMUM_CHANGES | def minRemove ( arr , n ) :
    LIS = [ 0 for i in range ( n ) ]
    len = 0
    for i in range ( n ) :
        LIS [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ i ] > arr [ j ] and ( i - j ) <= ( arr [ i ] - arr [ j ] ) ) :
                LIS [ i ] = max ( LIS [ i ] , LIS [ j ] + 1 )
        len = max ( len , LIS [ i ] )
    return ( n - len )

COUNTING_PAIRS_PERSON_CAN_FORM_PAIR_ONE_1 | def numberOfWays ( x ) :
    dp = [ 0 for _ in range (x + 1)]
    dp[0] = dp[1] = 1
    for i in range(2, x + 1):
        dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]
    return dp[x]

COUNT_1S_SORTED_BINARY_ARRAY | def countOnes ( arr , low , high ) :
    if high >= low :
        mid = int ( low + ( high - low ) / 2 )
        if ( ( mid == high or arr [ mid + 1 ] == 0 ) and ( arr [ mid ] == 1 ) ) :
            return mid + 1
        if arr [ mid ] == 1 :
            return countOnes ( arr , ( mid + 1 ) , high )
        return countOnes ( arr , low , mid - 1 )
    return 0

COUNT_ARRAYS_CONSECUTIVE_ELEMENT_DIFFERENT_VALUES | def countarray ( n , k , x ) :
    dp = list ( )
    dp.append ( 0 )
    dp.append ( 1 )
    i = 2
    while i < n :
        dp.append ( ( k - 2 ) * dp [ i - 1 ] + ( k - 1 ) * dp [ i - 2 ] )
        i = i + 1
    return ( ( k - 1 ) * dp [ n - 2 ] if x == 1 else dp [ n - 1 ] )

COUNT_BALANCED_BINARY_TREES_HEIGHT_H | def countBT ( h ) :
    MOD = 1000000007
    dp = [ 0 for i in range ( h + 1 ) ]
    dp [ 0 ] = 1
    dp [ 1 ] = 1
    for i in range ( 2 , h + 1 ) :
        dp [ i ] = ( dp [ i - 1 ] * ( ( 2 * dp [ i - 2 ] ) % MOD + dp [ i - 1 ] ) % MOD ) % MOD
    return dp [ h ]

COUNT_BINARY_DIGIT_NUMBERS_SMALLER_N | def countOfBinaryNumberLessThanN ( N ) :
    q = collections . deque ( )
    q.append ( 1 )
    cnt = 0
    while ( q ) :
        t = q.popleft ( )
        if ( t <= N ) :
            cnt = cnt + 1
            q.append ( t * 10 )
            q.append ( t * 10 + 1 )
    return cnt

COUNT_BINARY_STRINGS_K_TIMES_APPEARING_ADJACENT_TWO_SET_BITS | def countStrings ( n , k ) :
    dp = [ [ [ 0 , 0 ] for __ in range ( k + 1 ) ] for _ in range ( n + 1 ) ]
    dp [ 1 ] [ 0 ] [ 0 ] = 1
    dp [ 1 ] [ 0 ] [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( k + 1 ) :
            if j >= i:
                break
            else:
                dp [ i ] [ j ] [ 0 ] = ( dp [ i - 1 ] [ j ] [ 0 ] + dp [ i - 1 ] [ j ] [ 1 ] )
                dp [ i ] [ j ] [ 1 ] = dp [ i - 1 ] [ j ] [ 0 ]
                if j >= 1 :
                    dp [ i ] [ j ] [ 1 ] += dp [ i - 1 ] [ j - 1 ] [ 1 ]
    return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ]

COUNT_CHARACTERS_STRING_DISTANCE_ENGLISH_ALPHABETS | def countPairs ( str ) :
    result = 0 ;
    n = len ( str )
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if ( abs ( ord ( str [ i ] ) - ord ( str [ j ] ) ) == abs ( i - j ) ) :
                result += 1 ;
    return result ;

COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION_1 | def countDer ( n ) :
    der = [ 0 for i in range ( n + 1 ) ]
    der [ 0 ] = 1
    der [ 1 ] = 0
    der [ 2 ] = 1
    for i in range ( 3 , n + 1 ) :
        der [ i ] = ( i - 1 ) * ( der [ i - 1 ] + der [ i - 2 ] )
    return der [ n ]

COUNT_DIGITS_FACTORIAL_SET_1 | def findDigits ( n ) :
    if ( n < 0 ) :
        return 0
    if ( n <= 1 ) :
        return 1
    digits = 0
    for i in range ( 2 , n + 1 ) :
        digits += math.log10 ( i )
    return math.floor ( digits ) + 1

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2 | def countSolutions ( n ) :
    res = 0
    x = 0
    while ( x * x < n ) :
        y = 0
        while ( x * x + y * y < n ) :
            res = res + 1
            y = y + 1
        x = x + 1
    return res

COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2_1 | def countSolutions ( n ) :
    x = 0
    res = 0
    yCount = 0
    while ( yCount * yCount < n ) :
        yCount = yCount + 1
    while ( yCount != 0 ) :
        res = res + yCount
        x = x + 1
        while ( yCount != 0 and ( x * x + ( yCount - 1 ) * ( yCount - 1 ) >= n ) ) :
            yCount = yCount - 1
    return res

COUNT_DISTINCT_OCCURRENCES_AS_A_SUBSEQUENCE | def findSubsequenceCount ( S , T ) :
    m = len ( T )
    n = len ( S )
    if m > n :
        return 0
    mat = [ [ 0 for _ in range ( n + 1 ) ] for __ in range ( m + 1 ) ]
    for i in range ( 1 , m + 1 ) :
        mat [ i ] [ 0 ] = 0
    for j in range ( n + 1 ) :
        mat [ 0 ] [ j ] = 1
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if T [ i - 1 ] != S [ j - 1 ] :
                mat [ i ] [ j ] = mat [ i ] [ j - 1 ]
            else :
                mat [ i ] [ j ] = ( mat [ i ] [ j - 1 ] + mat [ i - 1 ] [ j - 1 ] )
    return mat [ m ] [ n ]

COUNT_ENTRIES_EQUAL_TO_X_IN_A_SPECIAL_MATRIX | def count ( n , x ) :
    cnt = 0
    for i in range ( 1 , n + 1 ) :
        if i <= x :
            if x // i <= n and x % i == 0 :
                cnt += 1
    return cnt

COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS_1 | def countSeq ( n ) :
    nCr = 1
    res = 1
    for r in range ( 1 , n + 1 ) :
        nCr = int ( ( nCr * ( n + 1 - r ) ) / r )
        res += nCr * nCr 
    return res 

COUNT_FREQUENCY_K_MATRIX_SIZE_N_MATRIXI_J_IJ | def find ( n , k ) :
    if ( n + 1 >= k ) :
        return ( k - 1 )
    else :
        return ( 2 * n + 1 - k )

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY | def countPairs ( arr , n ) :
    ans = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if ( arr [ i ] == arr [ j ] ) :
                ans += 1
    return ans

COUNT_INDEX_PAIRS_EQUAL_ELEMENTS_ARRAY_1 | def countPairs ( arr , n ) :
    mp = dict ( )
    for i in range ( n ) :
        if arr [ i ] in mp.keys ( ) :
            mp [ arr [ i ] ] += 1
        else :
            mp [ arr [ i ] ] = 1
    ans = 0
    for it in mp :
        count = mp [ it ]
        ans += ( count * ( count - 1 ) ) // 2
    return ans

COUNT_INVERSIONS_OF_SIZE_THREE_IN_A_GIVE_ARRAY_1 | def getInvCount ( arr , n ) :
    invcount = 0
    for i in range ( 1 , n - 1 ) :
        small = 0
        for j in range ( i + 1 , n ) :
            if ( arr [ i ] > arr [ j ] ) :
                small += 1
        great = 0
        for j in range ( i - 1 , - 1 , - 1 ) :
            if ( arr [ i ] < arr [ j ] ) :
                great += 1
        invcount += great * small
    return invcount

COUNT_MINIMUM_NUMBER_SUBSETS_SUBSEQUENCES_CONSECUTIVE_NUMBERS | def numofsubset ( arr , n ) :
    x = sorted ( arr )
    count = 1
    for i in range ( 0 , n - 1 ) :
        if ( x [ i ] + 1 != x [ i + 1 ] ) :
            count = count + 1
    return count

COUNT_NATURAL_NUMBERS_WHOSE_PERMUTATION_GREATER_NUMBER | def countNumber ( n ) :
    result = 0
    for i in range ( 1 , 10 ) :
        s = [ ]
        if ( i <= n ) :
            s.append ( i )
            result += 1
        while len ( s ) != 0 :
            tp = s [ - 1 ]
            s.pop ( )
            for j in range ( tp % 10 , 10 ) :
                x = tp * 10 + j
                if ( x <= n ) :
                    s.append ( x )
                    result += 1
    return result

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX | def countNegative ( M , n , m ) :
    count = 0
    for i in range ( n ) :
        for j in range ( m ) :
            if M [ i ] [ j ] < 0 :
                count += 1
            else :
                break
    return count

COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX_1 | def countNegative ( M , n , m ) :
    count = 0
    i = 0
    j = m - 1
    while j >= 0 and i < n :
        if M [ i ] [ j ] < 0 :
            count += ( j + 1 )
            i += 1
        else :
            j -= 1
    return count

COUNT_NUMBERS_CAN_CONSTRUCTED_USING_TWO_NUMBERS | def countNums ( n , x , y ) :
    arr = [ False for i in range ( n + 2 ) ]
    if ( x <= n ) :
        arr [ x ] = True
    if ( y <= n ) :
        arr [ y ] = True
    result = 0
    for i in range ( min ( x , y ) , n + 1 ) :
        if ( arr [ i ] ) :
            if ( i + x <= n ) :
                arr [ i + x ] = True
            if ( i + y <= n ) :
                arr [ i + y ] = True
            result = result + 1
    return result

COUNT_NUMBER_BINARY_STRINGS_WITHOUT_CONSECUTIVE_1S | def countStrings ( n ) :
    a = [ 0 for i in range ( n ) ]
    b = [ 0 for i in range ( n ) ]
    a [ 0 ] = b [ 0 ] = 1
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    return a [ n - 1 ] + b [ n - 1 ]

COUNT_NUMBER_INCREASING_SUBSEQUENCES_SIZE_K | def numOfIncSubseqOfSizeK ( arr , n , k ) :
    dp = [ [ 0 for i in range ( n ) ] for i in range ( k ) ]
    for i in range ( n ) :
        dp [ 0 ] [ i ] = 1
    for l in range ( 1 , k ) :
        for i in range ( l , n ) :
            dp [ l ] [ i ] = 0
            for j in range ( l - 1 , i ) :
                if ( arr [ j ] < arr [ i ] ) :
                    dp [ l ] [ i ] += dp [ l - 1 ] [ j ]
    Sum = 0
    for i in range ( k - 1 , n ) :
        Sum += dp [ k - 1 ] [ i ]
    return Sum

COUNT_NUMBER_OF_OCCURRENCES_OR_FREQUENCY_IN_A_SORTED_ARRAY | def countOccurrences ( arr , n , x ) :
    res = 0
    for i in range ( n ) :
        if x == arr [ i ] :
            res += 1
    return res

COUNT_NUMBER_OF_STRINGS_MADE_OF_R_G_AND_B_USING_GIVEN_COMBINATION | def possibleStrings ( n , r , b , g ) :
    fact = [ 0 for i in range ( n + 1 ) ]
    fact [ 0 ] = 1
    for i in range ( 1 , n + 1 , 1 ) :
        fact [ i ] = fact [ i - 1 ] + i
    left = n - ( r + g + b )
    sum = 0
    for i in range ( 0 , left + 1 , 1 ) :
        for j in range ( 0 , left - i + 1 , 1 ) :
            k = left - ( i + j )
            sum = int ( sum + fact [ n ] / ( fact [ i + r ] + fact [ j + b ] + fact [ k + g ] ) )
    return sum

COUNT_NUMBER_OF_WAYS_TO_PARTITION_A_SET_INTO_K_SUBSETS_1 | def countP ( n , k ) :
    dp = [ [ 0 for i in range ( k + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        dp [ i ] [ 0 ] = 0
    for i in range ( k + 1 ) :
        dp [ 0 ] [ k ] = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , k + 1 ) :
            if ( j == 1 or i == j ) :
                dp [ i ] [ j ] = 1
            else :
                dp [ i ] [ j ] = ( j * dp [ i - 1 ] [ j ] + dp [ i - 1 ] [ j - 1 ] )
    return dp [ n ] [ k ]

COUNT_NUMBER_PAIRS_N_B_N_GCD_B_B | def CountPairs ( n ) :
    k = n
    imin = 1
    ans = 0
    while ( imin <= n ) :
        imax = int ( n / k )
        ans += k * ( imax - imin + 1 )
        imin = imax + 1
        k = int ( n / imin )
    return ans

COUNT_NUMBER_WAYS_REACH_GIVEN_SCORE_GAME | def count ( n ) :
    table = [ 0 for i in range ( n + 1 ) ]
    table [ 0 ] = 1
    for i in range ( 3 , n + 1 ) :
        table [ i ] += table [ i - 3 ]
    for i in range ( 5 , n + 1 ) :
        table [ i ] += table [ i - 5 ]
    for i in range ( 10 , n + 1 ) :
        table [ i ] += table [ i - 10 ]
    return table [ n ]

COUNT_NUMBER_WAYS_TILE_FLOOR_SIZE_N_X_M_USING_1_X_M_SIZE_TILES | def countWays ( n , m ) :
    count = [ ]
    for i in range ( n + 2 ) :
        count.append ( 0 )
    count [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        if ( i > m ) :
            count [ i ] = count [ i - 1 ] + count [ i - m ]
        elif ( i < m ) :
            count [ i ] = 1
        else :
            count [ i ] = 2
    return count [ n ]

COUNT_OF_SUB_STRINGS_THAT_DO_NOT_CONTAIN_ALL_THE_CHARACTERS_FROM_THE_SET_A_B_C_AT_THE_SAME_TIME | def CountSubString ( str , n ) :
    ans = ( n * ( n + 1 ) ) // 2
    a_index = 0
    b_index = 0
    c_index = 0
    for i in range ( n ) :
        if ( str [ i ] == 'a' ) :
            a_index = i + 1
            ans -= min ( b_index , c_index )
        elif ( str [ i ] == 'b' ) :
            b_index = i + 1
            ans -= min ( a_index , c_index )
        else :
            c_index = i + 1
            ans -= min ( a_index , b_index )
    return ans

COUNT_OPERATIONS_MAKE_STRINGAB_FREE | def abFree ( s ) :
    b_count = 0
    res = 0
    for i in range ( len ( s ) ) :
        if s [ ~ i ] == 'a' :
            res = ( res + b_count )
            b_count = ( b_count * 2 )
        else :
            b_count += 1
    return res

COUNT_PAIRS_DIFFERENCE_EQUAL_K | def countPairsWithDiffK ( arr , n , k ) :
    count = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            if arr [ i ] - arr [ j ] == k or arr [ j ] - arr [ i ] == k :
                count += 1
    return count

COUNT_PAIRS_DIFFERENCE_EQUAL_K_1 | def countPairsWithDiffK ( arr , n , k ) :
    count = 0
    arr.sort ( )
    l = 0
    r = 0
    while r < n :
        if arr [ r ] - arr [ l ] == k :
            count += 1
            l += 1
            r += 1
        elif arr [ r ] - arr [ l ] > k :
            l += 1
        else :
            r += 1
    return count

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X | def countPairs ( arr1 , arr2 , m , n , x ) :
    count = 0
    for i in range ( m ) :
        for j in range ( n ) :
            if arr1 [ i ] + arr2 [ j ] == x :
                count = count + 1
    return count

COUNT_PAIRS_TWO_SORTED_ARRAYS_WHOSE_SUM_EQUAL_GIVEN_VALUE_X_1 | def countPairs ( arr1 , arr2 , m , n , x ) :
    count = 0
    us = set ( )
    for i in range ( m ) :
        us.add ( arr1 [ i ] )
    for j in range ( n ) :
        if x - arr2 [ j ] in us :
            count += 1
    return count

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY | def countPairs ( arr , n ) :
    result = 0 ;
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            product = arr [ i ] * arr [ j ] ;
            for k in range ( 0 , n ) :
                if ( arr [ k ] == product ) :
                    result = result + 1 ;
                    break ;
    return result ;

COUNT_PAIRS_WHOSE_PRODUCTS_EXIST_IN_ARRAY_1 | def countPairs ( arr , n ) :
    result = 0
    Hash = set ( )
    for i in range ( n ) :
        Hash.add ( arr [ i ] )
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            product = arr [ i ] * arr [ j ]
            if product in ( Hash ) :
                result += 1
    return result

COUNT_PALINDROME_SUB_STRINGS_STRING | def CountPS ( str , n ) :
    dp = [ [ 0 for x in range ( n ) ] for y in range ( n ) ]
    P = [ [ False for x in range ( n ) ] for y in range ( n ) ]
    for i in range ( n ) :
        P [ i ] [ i ] = True
    for i in range ( n - 1 ) :
        if ( str [ i ] == str [ i + 1 ] ) :
            P [ i ] [ i + 1 ] = True
            dp [ i ] [ i + 1 ] = 1
    for gap in range ( 2 , n ) :
        for i in range ( n - gap ) :
            j = gap + i ;
            if ( str [ i ] == str [ j ] and P [ i + 1 ] [ j - 1 ] ) :
                P [ i ] [ j ] = True
            if ( P [ i ] [ j ] == True ) :
                dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] + 1 - dp [ i + 1 ] [ j - 1 ] )
            else :
                dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i + 1 ] [ j ] - dp [ i + 1 ] [ j - 1 ] )
    return dp [ 0 ] [ n - 1 ]

COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING | def countPS ( str ) :
    N = len ( str )
    cps = [ [ 0 for i in range ( N + 2 ) ] for j in range ( N + 2 ) ]
    for i in range ( N ) :
        cps [ i ] [ i ] = 1
    for L in range ( 2 , N + 1 ) :
        for i in range ( N ) :
            k = L + i - 1
            if ( k < N ) :
                if ( str [ i ] == str [ k ] ) :
                    cps [ i ] [ k ] = ( cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] + 1 )
                else :
                    cps [ i ] [ k ] = ( cps [ i ] [ k - 1 ] + cps [ i + 1 ] [ k ] - cps [ i + 1 ] [ k - 1 ] )
    return cps [ 0 ] [ N - 1 ]

COUNT_POSSIBLE_DECODINGS_GIVEN_DIGIT_SEQUENCE_1 | def countDecodingDP ( digits , n ) :
    count = [ 0 ] * ( n + 1 )
    count [ 0 ] = 1
    count [ 1 ] = 1
    if digits [ 0 ] == '0' :
        return 0
    for i in range ( 2 , n + 1 ) :
        count [ i ] = 0
        if ( digits [ i - 1 ] > '0' ) :
            count [ i ] = count [ i - 1 ]
        if ( digits [ i - 2 ] == '1' or ( digits [ i - 2 ] == '2' and digits [ i - 1 ] < '7' ) ) :
            count [ i ] += count [ i - 2 ]
    return count [ n ]

COUNT_POSSIBLE_GROUPS_SIZE_2_3_SUM_MULTIPLE_3 | def findgroups ( arr , n ) :
    c = [ 0 , 0 , 0 ]
    res = 0
    for i in range ( 0 , n ) :
        c [ arr [ i ] % 3 ] += 1
    res += ( ( c [ 0 ] * ( c [ 0 ] - 1 ) ) >> 1 )
    res += c [ 1 ] * c [ 2 ]
    res += ( c [ 0 ] * ( c [ 0 ] - 1 ) * ( c [ 0 ] - 2 ) ) / 6
    res += ( c [ 1 ] * ( c [ 1 ] - 1 ) * ( c [ 1 ] - 2 ) ) / 6
    res += ( ( c [ 2 ] * ( c [ 2 ] - 1 ) * ( c [ 2 ] - 2 ) ) / 6 )
    res += c [ 0 ] * c [ 1 ] * c [ 2 ]
    return res

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_1 | def numberOfPaths ( m , n ) :
    count = [ [ 0 for x in range ( m ) ] for y in range ( n ) ]
    for i in range ( m ) :
        count [ i ] [ 0 ] = 1 ;
    for j in range ( n ) :
        count [ 0 ] [ j ] = 1 ;
    for i in range ( 1 , m ) :
        for j in range ( n ) :
            count [ i ] [ j ] = count [ i - 1 ] [ j ] + count [ i ] [ j - 1 ]
    return count [ m - 1 ] [ n - 1 ]

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_2 | def numberOfPaths ( m , n ) :
    dp = [ 0 for i in range ( n ) ]
    dp[0]=1
    for i in range ( m  ) :
        for j in range ( 1 , n ) :
            dp [ j ] += dp [ j - 1 ]
    return dp [ n - 1 ]

COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_3 | def numberOfPaths ( m , n ) :
    for i in range ( n , ( m + n - 1 ) ) :
        path *= i
        path //= ( i - n + 1 )
    return path

COUNT_ROTATIONS_DIVISIBLE_4 | def countRotations ( n ) :
    l = len ( n )
    if ( l == 1 ) :
        oneDigit = ( int ) ( n [ 0 ] )
        if ( oneDigit % 4 == 0 ) :
            return 1
        return 0
    count = 0
    for i in range ( 0 , l - 1 ) :
        twoDigit = ( int ) ( n [ i ] ) * 10 + ( int ) ( n [ i + 1 ] )
        if ( twoDigit % 4 == 0 ) :
            count = count + 1
    twoDigit = ( int ) ( n [ l - 1 ] ) * 10 + ( int ) ( n [ 0 ] )
    if ( twoDigit % 4 == 0 ) :
        count = count + 1
    return count

COUNT_ROTATIONS_DIVISIBLE_8 | def countRotationsDivBy8 ( n ) :
    l = len ( n )
    count = 0
    if ( l == 1 ) :
        oneDigit = int ( n [ 0 ] )
        if ( oneDigit % 8 == 0 ) :
            return 1
        return 0
    if ( l == 2 ) :
        first = int ( n [ 0 ] ) * 10 + int ( n [ 1 ] )
        second = int ( n [ 1 ] ) * 10 + int ( n [ 0 ] )
        if ( first % 8 == 0 ) :
            count += 1
        if ( second % 8 == 0 ) :
            count += 1
        return count
    threeDigit = 0
    for i in range ( 0 , ( l - 2 ) ) :
        threeDigit = ( int ( n [ i ] ) * 100 + int ( n [ i + 1 ] ) * 10 + int ( n [ i + 2 ] ) )
        if ( threeDigit % 8 == 0 ) :
            count += 1
    threeDigit = ( int ( n [ l - 1 ] ) * 100 + int ( n [ 0 ] ) * 10 + int ( n [ 1 ] ) )
    if ( threeDigit % 8 == 0 ) :
        count += 1
    threeDigit = ( int ( n [ l - 2 ] ) * 100 + int ( n [ l - 1 ] ) * 10 + int ( n [ 0 ] ) )
    if ( threeDigit % 8 == 0 ) :
        count += 1
    return count

COUNT_SET_BITS_IN_AN_INTEGER_1 | def countSetBits ( n ) :
    if ( n == 0 ) :
        return 0
    else :
        return ( n & 1 ) + countSetBits ( n >> 1 )

COUNT_SET_BITS_IN_AN_INTEGER_2 | def countSetBits ( n ) :
    count = 0
    while ( n ) :
        n &= ( n - 1 )
        count += 1
    return count

COUNT_SET_BITS_IN_AN_INTEGER_3 | def countSetBits ( n ) :
    if ( n == 0 ) :
        return 0
    else :
        return 1 + countSetBits ( n & ( n - 1 ) )

COUNT_SORTED_ROWS_MATRIX | def sortedCount ( mat , r , c ) :
    result = 0
    for i in range ( r ) :
        j = 0
        for j in range ( c - 1 ) :
            if mat [ i ] [ j + 1 ] <= mat [ i ] [ j ] :
                break
        if j == c - 2 :
            result += 1
    for i in range ( 0 , r ) :
        j = 0
        for j in range ( c - 1 , 0 , - 1 ) :
            if mat [ i ] [ j - 1 ] <= mat [ i ] [ j ] :
                break
        if c > 1 and j == 1 :
            result += 1
    return result

COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS_1 | def countStr ( n ) :
    return ( 1 + ( n * 2 ) + ( n * ( ( n * n ) - 1 ) // 2 ) )

COUNT_STRINGS_WITH_CONSECUTIVE_1S | def countStrings ( n ) :
    a = [ 0 ] * n
    b = [ 0 ] * n
    a [ 0 ] = b [ 0 ] = 1
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    return ( 1 << n ) - a [ n - 1 ] - b [ n - 1 ]

COUNT_SUBARRAYS_WITH_SAME_EVEN_AND_ODD_ELEMENTS | def countSubarrays ( arr , n ) :
    difference = 0
    ans = 0
    hash_positive = [ 0 ] * ( n + 1 )
    hash_negative = [ 0 ] * ( n + 1 )
    hash_positive [ 0 ] = 1
    for i in range ( n ) :
        if ( arr [ i ] & 1 == 1 ) :
            difference = difference + 1
        else :
            difference = difference - 1
        if ( difference < 0 ) :
            ans += hash_negative [ - difference ]
            hash_negative [ - difference ] = hash_negative [ - difference ] + 1
        else :
            ans += hash_positive [ difference ]
            hash_positive [ difference ] = hash_positive [ difference ] + 1
    return ans

COUNT_SUBSTRINGS_WITH_SAME_FIRST_AND_LAST_CHARACTERS | def countSubstringWithEqualEnds ( s ) :
    result = 0
    n = len ( s )
    for i in range ( n ) :
        for j in range ( i , n ) :
            if ( s [ i ] == s [ j ] ) :
                result = result + 1
    return result

COUNT_TOTAL_SET_BITS_IN_ALL_NUMBERS_FROM_1_TO_N | def countSetBits ( n ) :
    i = 0
    ans = 0
    while ( ( 1 << i ) <= n ) :
        k = 0
        change = 1 << i
        for j in range ( 0 , n + 1 ) :
            ans += k
            if change == 1 :
                k = not k
                change = 1 << i
            else :
                change -= 1
        i += 1
    return ans

COUNT_TRAILING_ZEROES_FACTORIAL_NUMBER | def findTrailingZeros ( n ) :
    count = 0
    i = 5
    while ( n / i >= 1 ) :
        count += int ( n / i )
        i *= 5
    return int ( count )

COUNT_WAYS_BUILD_STREET_GIVEN_CONSTRAINTS | def countWays ( n ) :
    dp = [ [ 0 ] * ( n + 1 ) for i in range ( 2 ) ]
    dp [ 0 ] [ 1 ] = 1
    dp [ 1 ] [ 1 ] = 2
    for i in range ( 2 , n + 1 ) :
        dp [ 0 ] [ i ] = dp [ 0 ] [ i - 1 ] + dp [ 1 ] [ i - 1 ]
        dp [ 1 ] [ i ] = ( dp [ 0 ] [ i - 1 ] * 2 + dp [ 1 ] [ i - 1 ] )
    return dp [ 0 ] [ n ] + dp [ 1 ] [ n ]

COUNT_WAYS_DIVIDE_CIRCLE_USING_N_NON_INTERSECTING_CHORDS | def chordCnt ( A ) :
    n = 2 * A
    dpArray = [ 0 ] * ( n + 1 )
    dpArray [ 0 ] = 1
    dpArray [ 2 ] = 1
    for i in range ( 4 , n + 1 , 2 ) :
        for j in range ( 0 , i - 1 , 2 ) :
            dpArray [ i ] += ( dpArray [ j ] * dpArray [ i - 2 - j ] )
    return int ( dpArray [ n ] )

COUNT_WORDS_APPEAR_EXACTLY_TWO_TIMES_ARRAY_WORDS | def countWords ( str , n ) :
    m = dict ( )
    for i in range ( n ) :
        m [ str [ i ] ] = m.get ( str [ i ] , 0 ) + 1
    res = 0
    for i in m.values ( ) :
        if i == 2 :
            res += 1
    return res

COUNT_WORDS_WHOSE_TH_LETTER_EITHER_1_TH_TH_I1_TH_LETTER_GIVEN_WORD | def countWords ( str , l ) :
    count = 1 ;
    if ( l == 1 ) :
        return count
    if ( str [ 0 ] == str [ 1 ] ) :
        count *= 1
    else :
        count *= 2
    for j in range ( 1 , l - 1 ) :
        if ( str [ j ] == str [ j - 1 ] and str [ j ] == str [ j + 1 ] ) :
            count *= 1
        elif ( str [ j ] == str [ j - 1 ] or str [ j ] == str [ j + 1 ] or str [ j - 1 ] == str [ j + 1 ] ) :
            count *= 2
        else :
            count *= 3
    if ( str [ l - 1 ] == str [ l - 2 ] ) :
        count *= 1
    else :
        count *= 2
    return count

C_PROGRAM_CONCATENATE_STRING_GIVEN_NUMBER_TIMES | def repeat ( s , n ) :
    s1 = s
    for i in range ( 1 , n ) :
        s += s1
    return s

C_PROGRAM_FACTORIAL_NUMBER | def factorial ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * factorial ( n - 1 )

C_PROGRAM_FIND_LARGEST_ELEMENT_ARRAY_1 | def largest ( arr , n ) :
    return sorted(arr[:n], reverse=False)[n-1]

C_PROGRAM_FIND_SECOND_FREQUENT_CHARACTER | def getSecondMostFreq ( str ) :
    NO_OF_CHARS = 256
    count = [ 0 ] * NO_OF_CHARS
    for i in range ( len ( str ) ) :
        count [ ord ( str [ i ] ) ] += 1
    first , second = 0 , 0
    for i in range ( NO_OF_CHARS ) :
        if count [ i ] > count [ first ] :
            second = first
            first = i
        elif ( count [ i ] > count [ second ] and count [ i ] != count [ first ] ) :
            second = i
    return chr ( second )

DECIMAL_BINARY_CONVERSION_WITHOUT_USING_ARITHMETIC_OPERATORS | def decToBin ( n ) :
    if ( n == 0 ) :
        return "0"
    bin = ""
    while ( n > 0 ) :
        if ( n & 1 == 0 ) :
            bin = '0' + bin
        else :
            bin = '1' + bin
        n = n >> 1
    return bin

DECODE_STRING_RECURSIVELY_ENCODED_COUNT_FOLLOWED_SUBSTRING | def decode ( Str ) :
    integerstack = [ ]
    stringstack = [ ]
    temp = ""
    result = ""
    for i in range ( len ( Str ) ) :
        count = 0
        if ( Str [ i ] >= '0' and Str [ i ] <= '9' ) :
            while ( Str [ i ] >= '0' and Str [ i ] <= '9' ) :
                count = count * 10 + ord ( Str [ i ] ) - ord ( '0' )
                i += 1
            i -= 1
            integerstack.append ( count )
        elif ( Str [ i ] == ']' ) :
            temp = ""
            count = 0
            if ( len ( integerstack ) != 0 ) :
                count = integerstack [ - 1 ]
                integerstack.pop ( )
            while ( len ( stringstack ) != 0 and stringstack [ - 1 ] != '[' ) :
                temp = stringstack [ - 1 ] + temp
                stringstack.pop ( )
            if ( len ( stringstack ) != 0 and stringstack [ - 1 ] == '[' ) :
                stringstack.pop ( )
            for j in range ( count ) :
                result = result + temp
            for j in range ( len ( result ) ) :
                stringstack.append ( result [ j ] )
            result = ""
        elif ( Str [ i ] == '[' ) :
            if ( Str [ i - 1 ] >= '0' and Str [ i - 1 ] <= '9' ) :
                stringstack.append ( Str [ i ] )
            else :
                stringstack.append ( Str [ i ] )
                integerstack.append ( 1 )
        else :
            stringstack.append ( Str [ i ] )
    while len ( stringstack ) != 0 :
        result = stringstack [ - 1 ] + result
        stringstack.pop ( )
    return result

DELANNOY_NUMBER_1 | def dealnnoy ( n , m ) :
    dp = [ [ 0 for x in range ( n + 1 ) ] for x in range ( m + 1 ) ]
    for i in range ( m + 1 ) :
        dp [ 0 ] [ i ] = 1
    for i in range ( m + 1 ) :
        dp [ i ] [ 0 ] = 1
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            dp [ i ] [ j ] = dp [ i - 1 ] [ j ] + dp [ i - 1 ] [ j - 1 ] + dp [ i ] [ j - 1 ]
    return dp [ m ] [ n ]

DETECT_IF_TWO_INTEGERS_HAVE_OPPOSITE_SIGNS | def oppositeSigns ( x , y ) :
    return ( ( x ^ y ) < 0 )

DIAGONALLY_DOMINANT_MATRIX | def isDDM ( m , n ) :
    for i in range ( 0 , n ) :
        sum = 0
        for j in range ( 0 , n ) :
            sum = sum + abs ( m [ i ] [ j ] )
        sum = sum - abs ( m [ i ] [ i ] )
        if ( abs ( m [ i ] [ i ] ) < sum ) :
            return False
    return True

DICE_THROW_PROBLEM | def findWays ( m , n , x ) :
    table = [ [ 0 ] * ( x + 1 ) for i in range ( n + 1 ) ]
    for j in range ( 1 , min ( m + 1 , x + 1 ) ) :
        table [ 1 ] [ j ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 1 , x + 1 ) :
            for k in range ( 1 , min ( m + 1 , j ) ) :
                table [ i ] [ j ] += table [ i - 1 ] [ j - k ]
    return table [ - 1 ] [ - 1 ]

DIFFERENCE_BETWEEN_HIGHEST_AND_LEAST_FREQUENCIES_IN_AN_ARRAY | def findDiff ( arr , n ) :
    arr.sort ( )
    count = 0
    max_count = 0
    min_count = n
    for i in range ( 0 , ( n - 1 ) ) :
        if arr [ i ] == arr [ i + 1 ] :
            count += 1
            continue
        else :
            max_count = max ( max_count , count )
            min_count = min ( min_count , count )
            count = 0
    return max_count - min_count

DIFFERENCE_BETWEEN_HIGHEST_AND_LEAST_FREQUENCIES_IN_AN_ARRAY_1 | def findDiff ( arr , n ) :
    mp = defaultdict ( lambda : 0 )
    for i in range ( n ) :
        mp [ arr [ i ] ] += 1
    max_count = 0
    min_count = n
    for key , values in mp.items ( ) :
        max_count = max ( max_count , values )
        min_count = min ( min_count , values )
    return max_count - min_count

DIFFERENT_WAYS_SUM_N_USING_NUMBERS_GREATER_EQUAL_M | def numberofways ( n , m ) :
    dp = np.zeros ( ( n + 2 , n + 2 ) )
    dp [ 0 ] [ n + 1 ] = 1
    for k in range ( n , m - 1 , - 1 ) :
        for i in range ( n + 1 ) :
            dp [ i ] [ k ] = dp [ i ] [ k + 1 ]
            if ( i - k >= 0 ) :
                dp [ i ] [ k ] = ( dp [ i ] [ k ] + dp [ i - k ] [ k ] )
    return dp [ n ] [ m ]

DISCRETE_LOGARITHM_FIND_INTEGER_K_AK_CONGRUENT_MODULO_B | def discreteLogarithm ( a , b , m ) :
    n = int ( math.sqrt ( m ) + 1 )
    an = 1
    for i in range ( n ) :
        an = ( an * a ) % m
    value = [ 0 ] * m
    cur = an
    for i in range ( 1 , n + 1 ) :
        if ( value [ cur ] == 0 ) :
            value [ cur ] = i
        cur = ( cur * an ) % m
    cur = b
    for i in range ( n + 1 ) :
        if ( value [ cur ] > 0 ) :
            ans = value [ cur ] * n - i
            if ( ans < m ) :
                return ans
        cur = ( cur * a ) % m
    return - 1

DISTRIBUTING_ITEMS_PERSON_CANNOT_TAKE_TWO_ITEMS_TYPE_1 | def checkCount ( arr , n , k ) :
    mp = defaultdict ( lambda : 0 )
    for i in range ( n ) :
        mp [ arr [ i ] ] += 1
    for key , values in mp.items ( ) :
        if values > 2 * k :
            return False
    return True

DISTRIBUTING_M_ITEMS_CIRCLE_SIZE_N_STARTING_K_TH_POSITION | def lastPosition ( n , m , k ) :
    if ( m <= n - k + 1 ) :
        return m + k - 1
    m = m - ( n - k + 1 )
    if ( m % n == 0 ) :
        return n
    else :
        return m % n

DIVIDE_LARGE_NUMBER_REPRESENTED_STRING | def longDivision ( number , divisor ) :
    ans = ""
    idx = 0
    temp = ord ( number [ idx ] ) - ord ( '0' )
    while ( temp < divisor ) :
        temp = ( temp * 10 + ord ( number [ idx + 1 ] ) - ord ( '0' ) )
        idx += 1
    while ( ( len ( number ) ) > idx ) :
        ans += chr ( math.floor ( temp // divisor ) + ord ( '0' ) )
        temp = ( ( temp % divisor ) * 10 + ord ( number [ idx + 1 ] ) - ord ( '0' ) )
        idx += 1
    ans += chr ( math.floor ( temp // divisor ) + ord ( '0' ) )
    if ( len ( ans ) == 0 ) :
        return "0"
    return ans

DIVISIBILITY_9_USING_BITWISE_OPERATORS | def isDivBy9 ( n ) :
    if ( n == 0 or n == 9 ) :
        return True
    if ( n < 9 ) :
        return False
    return isDivBy9 ( ( int ) ( n >> 3 ) - ( int ) ( n & 7 ) )

DIVISIBILITY_BY_12_FOR_A_LARGE_NUMBER | def isDvisibleBy12 ( num ) :
    if ( len ( num ) >= 3 ) :
        d1 = int ( num [ len ( num ) - 1 ] )
        if ( d1 % 2 != 0 ) :
            return False
        d2 = int ( num [ len ( num ) - 2 ] )
        sum = 0
        for i in range ( 0 , len ( num ) ) :
            sum += int ( num [ i ] )
        return ( sum % 3 == 0 and ( d2 * 10 + d1 ) % 4 == 0 )
    else :
        number = int ( num )
        return ( number % 12 == 0 )

DIVISIBILITY_BY_7 | def isDivisibleBy7 ( num ) :
    if num < 0 :
        return isDivisibleBy7 ( - num )
    if ( num == 0 or num == 7 ) :
        return True
    if ( num < 10 ) :
        return False
    return isDivisibleBy7 ( num // 10 - 2 * ( num - num // 10 * 10 ) )

DOUBLE_FACTORIAL_1 | def doublefactorial ( n ) :
    res = 1
    for i in range ( n , - 1 , - 2 ) :
        if ( i == 0 or i == 1 ) :
            return res
        else :
            res *= i
    return res;

DYNAMIC_PROGRAMMING_HIGH_EFFORT_VS_LOW_EFFORT_TASKS_PROBLEM | def maxTasks ( high , low , n ) :
    if ( n <= 0 ) :
        return 0
    return max ( high [ n - 1 ] + maxTasks ( high , low , ( n - 2 ) ) , low [ n - 1 ] + maxTasks ( high , low , ( n - 1 ) ) )

DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM | def knapSack ( W , wt , val , n ) :
    if n == 0 or W == 0 :
        return 0
    if ( wt [ n - 1 ] > W ) :
        return knapSack ( W , wt , val , n - 1 )
    else :
        return max ( val [ n - 1 ] + knapSack ( W - wt [ n - 1 ] , wt , val , n - 1 ) , knapSack ( W , wt , val , n - 1 ) )

DYNAMIC_PROGRAMMING_SET_11_EGG_DROPPING_PUZZLE_1 | def eggDrop ( n , k ) :
    eggFloor = [ [ 0 for x in range ( k + 1 ) ] for x in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        eggFloor [ i ] [ 1 ] = 1
        eggFloor [ i ] [ 0 ] = 0
    for j in range ( 1 , k + 1 ) :
        eggFloor [ 1 ] [ j ] = j
    for i in range ( 2 , n + 1 ) :
        for j in range ( 2 , k + 1 ) :
            eggFloor [ i ] [ j ] = INT_MAX
            for x in range ( 1 , j + 1 ) :
                res = 1 + max ( eggFloor [ i - 1 ] [ x - 1 ] , eggFloor [ i ] [ j - x ] )
                if res < eggFloor [ i ] [ j ] :
                    eggFloor [ i ] [ j ] = res
    return eggFloor [ n ] [ k ]

DYNAMIC_PROGRAMMING_SET_12_LONGEST_PALINDROMIC_SUBSEQUENCE | def lps ( seq ) :
    n = len ( seq )
    L = [ [ 0 for x in range ( n ) ] for x in range ( n ) ]
    for i in range ( n ) :
        L [ i ] [ i ] = 1
    for cl in range ( 2 , n + 1 ) :
        for i in range ( n - cl + 1 ) :
            j = i + cl - 1
            if seq [ i ] == seq [ j ] and cl == 2 :
                L [ i ] [ j ] = 2
            elif seq [ i ] == seq [ j ] :
                L [ i ] [ j ] = L [ i + 1 ] [ j - 1 ] + 2
            else :
                L [ i ] [ j ] = max ( L [ i ] [ j - 1 ] , L [ i + 1 ] [ j ] ) ;
    return L [ 0 ] [ n - 1 ]

DYNAMIC_PROGRAMMING_SET_14_MAXIMUM_SUM_INCREASING_SUBSEQUENCE | def maxSumIS ( arr , n ) :
    max = 0
    msis = [ 0 for x in range ( n ) ]
    for i in range ( n ) :
        msis [ i ] = arr [ i ]
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ i ] > arr [ j ] and msis [ i ] < msis [ j ] + arr [ i ] ) :
                msis [ i ] = msis [ j ] + arr [ i ]
    for i in range ( n ) :
        if max < msis [ i ] :
            max = msis [ i ]
    return max

DYNAMIC_PROGRAMMING_SET_15_LONGEST_BITONIC_SUBSEQUENCE | def lbs ( arr , n ) :
    lis = [ 1 for i in range ( n + 1 ) ]
    for i in range ( 1 , n ) :
        for j in range ( 0 , i ) :
            if ( ( arr [ i ] > arr [ j ] ) and ( lis [ i ] < lis [ j ] + 1 ) ) :
                lis [ i ] = lis [ j ] + 1
    lds = [ 1 for i in range ( n + 1 ) ]
    for i in reversed ( range ( n - 1 ) ) :
        for j in reversed ( range ( i - 1 , n ) ) :
            if ( arr [ i ] > arr [ j ] and lds [ i ] < lds [ j ] + 1 ) :
                lds [ i ] = lds [ j ] + 1
    maximum = lis [ 0 ] + lds [ 0 ] - 1
    for i in range ( 1 , n ) :
        maximum = max ( ( lis [ i ] + lds [ i ] - 1 ) , maximum )
    return maximum

DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING | def minPalPartion ( str ) :
    n = len ( str )
    C = [ [ 0 for i in range ( n ) ] for i in range ( n ) ]
    P = [ [ False for i in range ( n ) ] for i in range ( n ) ]
    j = 0
    k = 0
    L = 0
    for i in range ( n ) :
        P [ i ] [ i ] = True
        C [ i ] [ i ] = 0
    for L in range ( 2 , n + 1 ) :
        for i in range ( n - L + 1 ) :
            j = i + L - 1
            if L == 2 :
                P [ i ] [ j ] = ( str [ i ] == str [ j ] )
            else :
                P [ i ] [ j ] = ( ( str [ i ] == str [ j ] ) and P [ i + 1 ] [ j - 1 ] )
            if P [ i ] [ j ] == True :
                C [ i ] [ j ] = 0
            else :
                C [ i ] [ j ] = 100000000
                for k in range ( i , j ) :
                    C [ i ] [ j ] = min ( C [ i ] [ j ] , C [ i ] [ k ] + C [ k + 1 ] [ j ] + 1 )
    return C [ 0 ] [ n - 1 ]

DYNAMIC_PROGRAMMING_SET_28_MINIMUM_INSERTIONS_TO_FORM_A_PALINDROME | def findMinInsertions ( str , l , h ) :
    if ( l > h ) :
        return sys.maxsize
    if ( l == h ) :
        return 0
    if ( l == h - 1 ) :
        return 0 if ( str [ l ] == str [ h ] ) else 1
    if ( str [ l ] == str [ h ] ) :
        return findMinInsertions ( str , l + 1 , h - 1 )
    else :
        return ( min ( findMinInsertions ( str , l , h - 1 ) , findMinInsertions ( str , l + 1 , h ) ) + 1 )

DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT_1 | def maxProd ( n ) :
    if ( n == 2 or n == 3 ) :
        return ( n - 1 )
    res = 1
    while ( n > 4 ) :
        n -= 3
        res *= 3
    return ( n * res )

DYNAMIC_PROGRAMMING_SET_37_BOOLEAN_PARENTHESIZATION_PROBLEM | def countParenth ( symb , oper , n ) :
    F = [ [ 0 for i in range ( n + 1 ) ] for i in range ( n + 1 ) ]
    T = [ [ 0 for i in range ( n + 1 ) ] for i in range ( n + 1 ) ]
    for i in range ( n ) :
        if symb [ i ] == 'F' :
            F [ i ] [ i ] = 1
        else :
            F [ i ] [ i ] = 0
        if symb [ i ] == 'T' :
            T [ i ] [ i ] = 1
        else :
            T [ i ] [ i ] = 0
    for gap in range ( 1 , n ) :
        i = 0
        for j in range ( gap , n ) :
            T [ i ] [ j ] = F [ i ] [ j ] = 0
            for g in range ( gap ) :
                k = i + g
                tik = T [ i ] [ k ] + F [ i ] [ k ]
                tkj = T [ k + 1 ] [ j ] + F [ k + 1 ] [ j ]
                if oper [ k ] == '&' :
                    T [ i ] [ j ] += T [ i ] [ k ] * T [ k + 1 ] [ j ]
                    F [ i ] [ j ] += ( tik * tkj - T [ i ] [ k ] * T [ k + 1 ] [ j ] )
                if oper [ k ] == '|' :
                    F [ i ] [ j ] += F [ i ] [ k ] * F [ k + 1 ] [ j ]
                    T [ i ] [ j ] += ( tik * tkj - F [ i ] [ k ] * F [ k + 1 ] [ j ] )
                if oper [ k ] == '^' :
                    T [ i ] [ j ] += ( F [ i ] [ k ] * T [ k + 1 ] [ j ] + T [ i ] [ k ] * F [ k + 1 ] [ j ] )
                    F [ i ] [ j ] += ( T [ i ] [ k ] * T [ k + 1 ] [ j ] + F [ i ] [ k ] * F [ k + 1 ] [ j ] )
            i += 1
    return T [ 0 ] [ n - 1 ]

DYNAMIC_PROGRAMMING_SET_3_LONGEST_INCREASING_SUBSEQUENCE_1 | def lis ( arr , n) :
    lis = [ 1 ] * n
    for i in range ( 1 , n ) :
        for j in range ( 0 , i ) :
            if arr [ i ] > arr [ j ] and lis [ i ] < lis [ j ] + 1 :
                lis [ i ] = lis [ j ] + 1
    maximum = 0
    for i in range ( n ) :
        maximum = max ( maximum , lis [ i ] )
    return maximum

DYNAMIC_PROGRAMMING_SET_8_MATRIX_CHAIN_MULTIPLICATION | def MatrixChainOrder ( p , i , j ) :
    if i == j :
        return 0
    _min = sys.maxsize
    for k in range ( i , j ) :
        count = ( MatrixChainOrder ( p , i , k ) + MatrixChainOrder ( p , k + 1 , j ) + p [ i - 1 ] * p [ k ] * p [ j ] )
        if count < _min :
            _min = count
    return _min

DYNAMIC_PROGRAMMING_SUBSET_SUM_PROBLEM_1 | def isSubsetSum ( set , n , sum ) :
    subset = ( [ [ False for i in range ( sum + 1 ) ] for i in range ( n + 1 ) ] )
    for i in range ( n + 1 ) :
        subset [ i ] [ 0 ] = True
    for i in range ( 1 , sum + 1 ) :
        subset [ 0 ] [ i ] = False
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , sum + 1 ) :
            if j < set [ i - 1 ] :
                subset [ i ] [ j ] = subset [ i - 1 ] [ j ]
            if j >= set [ i - 1 ] :
                subset [ i ] [ j ] = ( subset [ i - 1 ] [ j ] or subset [ i - 1 ] [ j - set [ i - 1 ] ] )
    return subset [ n ] [ sum ]

EFFICIENT_SEARCH_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_IS_1 | def search ( arr , n , x ) :
    i = 0
    while ( i <= n - 1 ) :
        if ( arr [ i ] == x ) :
            return i
        i += abs ( arr [ i ] - x )
    return - 1

EFFICIENT_WAY_CHECK_WHETHER_N_TH_FIBONACCI_NUMBER_MULTIPLE_10 | def isMultipleOf10 ( n ) :
    return ( n % 15 == 0 )

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY | def countNum ( arr , n ) :
    count = 0
    arr = arr[:n]
    arr.sort ( )
    for i in range ( 0 , n - 1 ) :
        if ( arr [ i ] != arr [ i + 1 ] and arr [ i ] != arr [ i + 1 ] - 1 ) :
            count += arr [ i + 1 ] - arr [ i ] - 1
    return count

ELEMENTS_TO_BE_ADDED_SO_THAT_ALL_ELEMENTS_OF_A_RANGE_ARE_PRESENT_IN_ARRAY_1 | def countNum ( arr , n ) :
    s = dict ( )
    count , maxm , minm = 0 , - 10 ** 9 , 10 ** 9
    for i in range ( n ) :
        s [ arr [ i ] ] = 1
        if ( arr [ i ] < minm ) :
            minm = arr [ i ]
        if ( arr [ i ] > maxm ) :
            maxm = arr [ i ]
    for i in range ( minm , maxm + 1 ) :
        if i not in s.keys ( ) :
            count += 1
    return count

EQUILIBRIUM_INDEX_OF_AN_ARRAY | def equilibrium ( arr , n) :
    leftsum = 0
    rightsum = 0
    for i in range ( n ) :
        leftsum = 0
        rightsum = 0
        for j in range ( i ) :
            leftsum += arr [ j ]
        for j in range ( i + 1 , n ) :
            rightsum += arr [ j ]
        if leftsum == rightsum :
            return i
    return - 1

EQUILIBRIUM_INDEX_OF_AN_ARRAY_1 | def equilibrium ( arr ,n) :
    total_sum = sum ( arr )
    leftsum = 0
    for i , num in enumerate ( arr ) :
        total_sum -= num
        if leftsum == total_sum :
            return i
        leftsum += num
    return - 1

EULERS_CRITERION_CHECK_IF_SQUARE_ROOT_UNDER_MODULO_P_EXISTS | def squareRootExists ( n , p ) :
    n = n % p
    for x in range ( 2 , p , 1 ) :
        if ( ( x * x ) % p == n ) :
            return True
    return False

EVEN_FIBONACCI_NUMBERS_SUM | def evenFibSum ( limit ) :
    if ( limit < 2 ) :
        return 0
    ef1 = 0
    ef2 = 2
    sm = ef1 + ef2
    while ( ef2 <= limit ) :
        ef3 = 4 * ef2 + ef1
        if ( ef3 > limit ) :
            break
        ef1 = ef2
        ef2 = ef3
        sm = sm + ef2
    return sm

FAST_MULTIPLICATION_METHOD_WITHOUT_USING_MULTIPLICATION_OPERATOR_RUSSIAN_PEASANTS_ALGORITHM | def russianPeasant ( a , b ) :
    res = 0
    while ( b > 0 ) :
        if ( b & 1 ) :
            res = res + a
        a = a << 1
        b = b >> 1
    return res

FIBONACCI_MODULO_P | def findMinZero ( p ) :
    first = 1
    second = 1
    number = 2
    next = 1
    while ( next ) :
        next = ( first + second ) % p
        first = second
        second = next
        number = number + 1
    return number

FINDING_POWER_PRIME_NUMBER_P_N | def PowerOFPINnfactorial ( n , p ) :
    ans = 0
    temp = p
    while ( temp <= n ) :
        ans += int(n / temp)
        temp = temp * p
    return ans

FINDING_POWER_PRIME_NUMBER_P_N_1 | def PowerOFPINnfactorial ( n , p ) :
    ans = 0
    temp = p
    while ( temp <= n ) :
        ans += n / temp
        temp = temp * p
    return int ( ans )

FIND_A_ROTATION_WITH_MAXIMUM_HAMMING_DISTANCE | def maxHamming ( arr , n ) :
    brr = [ 0 ] * ( 2 * n + 1 )
    for i in range ( n ) :
        brr [ i ] = arr [ i ]
    for i in range ( n ) :
        brr [ n + i ] = arr [ i ]
    maxHam = 0
    for i in range ( 1 , n ) :
        currHam = 0
        k = 0
        for j in range ( i , i + n ) :
            if brr [ j ] != arr [ k ] :
                currHam += 1
                k = k + 1
        if currHam == n :
            return n
        maxHam = max ( maxHam , currHam )
    return maxHam

FIND_A_TRIPLET_THAT_SUM_TO_A_GIVEN_VALUE | def find3Numbers ( A , arr_size , sum ) :
    for i in range ( 0 , arr_size - 2 ) :
        for j in range ( i + 1 , arr_size - 1 ) :
            for k in range ( j + 1 , arr_size ) :
                if A [ i ] + A [ j ] + A [ k ] == sum :
                    print ( "Triplet is" , A [ i ] , ", " , A [ j ] , ", " , A [ k ] )
                    return True
    return False

FIND_EXPRESSION_DUPLICATE_PARENTHESIS_NOT | def findDuplicateparenthesis ( string ) :
    Stack = [ ]
    for ch in string :
        if ch == ')' :
            top = Stack.pop ( )
            elementsInside = 0
            while top != '(' :
                elementsInside += 1
                top = Stack.pop ( )
            if elementsInside < 1 :
                return True
        else :
            Stack.append ( ch )
    return False

FIND_FIRST_NATURAL_NUMBER_WHOSE_FACTORIAL_DIVISIBLE_X | def firstFactorialDivisibleNumber ( x ) :
    i = 1
    fact = 1
    for i in range ( 1 , x ) :
        fact = fact * i
        if ( fact % x == 0 ) :
            break
    return i

FIND_HARMONIC_MEAN_USING_ARITHMETIC_MEAN_GEOMETRIC_MEAN | def compute ( a , b ) :
    AM = ( a + b ) / 2
    GM = math.sqrt ( a * b )
    HM = ( GM * GM ) / AM
    return HM

FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME | def findIndex ( n ) :
    if ( n <= 1 ) :
        return n
    a = 0
    b = 1
    c = 1
    res = 1
    while ( c < n ) :
        c = a + b
        res = res + 1
        a = b
        b = c
    return res

FIND_INDEX_OF_AN_EXTRA_ELEMENT_PRESENT_IN_ONE_SORTED_ARRAY | def findExtra ( arr1 , arr2 , n ) :
    for i in range ( 0 , n ) :
        if ( arr1 [ i ] != arr2 [ i ] ) :
            return i
    return n

FIND_LARGEST_D_IN_ARRAY_SUCH_THAT_A_B_C_D | def findLargestd ( S , n ) :
    found = False
    S = S[:n]
    S.sort ( )
    for i in range ( n - 1 , - 1 , - 1 ) :
        for j in range ( 0 , n ) :
            if ( i == j ) :
                continue
            for k in range ( j + 1 , n ) :
                if ( i == k ) :
                    continue
                for l in range ( k + 1 , n ) :
                    if ( i == l ) :
                        continue
                    if ( S [ i ] == S [ j ] + S [ k ] + S [ l ] ) :
                        found = True
                        return S [ i ]
    if ( found == False ) :
        return - 1

FIND_LARGEST_D_IN_ARRAY_SUCH_THAT_A_B_C_D_1 | def findFourElements ( arr , n ) :
    mp = dict ( )
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            mp [ arr [ i ] + arr [ j ] ] = ( i , j )
    d = - 10 ** 9
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            abs_diff = abs ( arr [ i ] - arr [ j ] )
            if abs_diff in mp.keys ( ) :
                p = mp [ abs_diff ]
                if ( p [ 0 ] != i and p [ 0 ] != j and p [ 1 ] != i and p [ 1 ] != j ) :
                    d = max ( d , max ( arr [ i ] , arr [ j ] ) )
    return d

FIND_LARGEST_PRIME_FACTOR_NUMBER | def maxPrimeFactors ( n ) :
    maxPrime = - 1
    while n % 2 == 0 :
        maxPrime = 2
        n >>= 1
    for i in range ( 3 , int ( math.sqrt ( n ) ) + 1 , 2 ) :
        while n % i == 0 :
            maxPrime = i
            n = n / i
    if n > 2 :
        maxPrime = n
    return int ( maxPrime )

FIND_LAST_DIGIT_FACTORIAL_DIVIDES_FACTORIAL_B | def computeLastDigit ( A , B ) :
    variable = 1
    if ( A == B ) :
        return 1
    elif ( ( B - A ) >= 5 ) :
        return 0
    else :
        for i in range ( A + 1 , B + 1 ) :
            variable = ( variable * ( i % 10 ) ) % 10
        return variable % 10

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH | def findMaxAverage ( arr , n , k ) :
    if k > n :
        return - 1
    csum = [ 0 ] * n
    csum [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        csum [ i ] = csum [ i - 1 ] + arr [ i ]
    max_sum = csum [ k - 1 ]
    max_end = k - 1
    for i in range ( k , n ) :
        curr_sum = csum [ i ] - csum [ i - k ]
        if curr_sum > max_sum :
            max_sum = curr_sum
            max_end = i
    return max_end - k + 1

FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH_1 | def findMaxAverage ( arr , n , k ) :
    if ( k > n ) :
        return - 1
    sum = arr [ 0 ]
    for i in range ( 1 , k ) :
        sum += arr [ i ]
    max_sum = sum
    max_end = k - 1
    for i in range ( k , n ) :
        sum = sum + arr [ i ] - arr [ i - k ]
        if ( sum > max_sum ) :
            max_sum = sum
            max_end = i
    return max_end - k + 1

FIND_MAXIMUM_DOT_PRODUCT_TWO_ARRAYS_INSERTION_0S | def MaxDotProduct ( A , B , m , n ) :
    dp = [ [ 0 for i in range ( m + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 , 1 ) :
        for j in range ( i , m + 1 , 1 ) :
            dp [ i ] [ j ] = max ( ( dp [ i - 1 ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) ) , dp [ i ] [ j - 1 ] )
    return dp [ n ] [ m ]

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY | def maxProduct ( arr , n ) :
    if n < 3 :
        return - 1
    max_product = - ( sys.maxsize - 1 )
    for i in range ( 0 , n - 2 ) :
        for j in range ( i + 1 , n - 1 ) :
            for k in range ( j + 1 , n ) :
                max_product = max ( max_product , arr [ i ] * arr [ j ] * arr [ k ] )
    return max_product

FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY_1 | def maxProduct ( arr , n ) :
    if n < 3 :
        return - 1
    arr.sort ( )
    return max ( arr [ 0 ] * arr [ 1 ] * arr [ n - 1 ] , arr [ n - 1 ] * arr [ n - 2 ] * arr [ n - 3 ] )

FIND_MAXIMUM_SUM_POSSIBLE_EQUAL_SUM_THREE_STACKS | def maxSum ( stack1 , stack2 , stack3 , n1 , n2 , n3 ) :
    sum1 , sum2 , sum3 = 0 , 0 , 0
    for i in range ( n1 ) :
        sum1 += stack1 [ i ]
    for i in range ( n2 ) :
        sum2 += stack2 [ i ]
    for i in range ( n3 ) :
        sum3 += stack3 [ i ]
    top1 , top2 , top3 = 0 , 0 , 0
    ans = 0
    while ( 1 ) :
        if ( top1 == n1 or top2 == n2 or top3 == n3 ) :
            return 0
        if ( sum1 == sum2 and sum2 == sum3 ) :
            return sum1
        if ( sum1 >= sum2 and sum1 >= sum3 ) :
            sum1 -= stack1 [ top1 ]
            top1 = top1 + 1
        elif ( sum2 >= sum3 and sum2 >= sum3 ) :
            sum2 -= stack2 [ top2 ]
            top2 = top2 + 1
        elif ( sum3 >= sum2 and sum3 >= sum1 ) :
            sum3 -= stack3 [ top3 ]
            top3 = top3 + 1

FIND_MEDIAN_ROW_WISE_SORTED_MATRIX | def binaryMedian ( m , r , d ) :
    mi = sys.maxsize
    mx = - sys.maxsize - 1
    for i in range ( r ) :
        if m [ i ] [ 0 ] < mi :
            mi = m [ i ] [ 0 ]
        if m [ i ] [ d - 1 ] > mx :
            mx = m [ i ] [ d - 1 ]
    desired = ( r * d + 1 ) // 2
    while ( mi < mx ) :
        mid = mi + ( mx - mi ) // 2
        place = [ 0 ]
        for i in range ( r ) :
            j = upper_bound ( m [ i ] , mid )
            place [ 0 ] = place [ 0 ] + j
        if place [ 0 ] < desired :
            mi = mid + 1
        else :
            mx = mid
    print ( "Median is" , mi )
    return

FIND_MINIMUM_DIFFERENCE_PAIR | def findMinDiff ( arr , n ) :
    diff = 10 ** 20
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if abs ( arr [ i ] - arr [ j ] ) < diff :
                diff = abs ( arr [ i ] - arr [ j ] )
    return diff

FIND_MINIMUM_DIFFERENCE_PAIR_1 | def findMinDiff ( arr , n ) :
    arr = arr[:n]
    arr = sorted ( arr )
    diff = 10 ** 20
    for i in range ( n - 1 ) :
        if arr [ i + 1 ] - arr [ i ] < diff :
            diff = arr [ i + 1 ] - arr [ i ]
    return diff

FIND_MINIMUM_ELEMENT_IN_A_SORTED_AND_ROTATED_ARRAY | def findMin ( arr , low , high ) :
    if high < low :
        return arr [ 0 ]
    if high == low :
        return arr [ low ]
    mid = int ( ( low + high ) / 2 )
    if mid < high and arr [ mid + 1 ] < arr [ mid ] :
        return arr [ mid + 1 ]
    if mid > low and arr [ mid ] < arr [ mid - 1 ] :
        return arr [ mid ]
    if arr [ high ] > arr [ mid ] :
        return findMin ( arr , low , mid - 1 )
    return findMin ( arr , mid + 1 , high )

FIND_MINIMUM_NUMBER_DIVIDED_MAKE_NUMBER_PERFECT_SQUARE | def findMinNumber ( n ) :
    count = 0
    ans = 1
    while n % 2 == 0 :
        count += 1
        n //= 2
    if count % 2 is not 0 :
        ans *= 2
    for i in range ( 3 , ( int ) ( math.sqrt ( n ) ) + 1 , 2 ) :
        count = 0
        while n % i == 0 :
            count += 1
            n //= i
        if count % 2 is not 0 :
            ans *= i
    if n > 2 :
        ans *= n
    return ans

FIND_MINIMUM_NUMBER_OF_COINS_THAT_MAKE_A_CHANGE_1 | def minCoins ( coins , m , V ) :
    table = [ 0 for i in range ( V + 1 ) ]
    table [ 0 ] = 0
    for i in range ( 1 , V + 1 ) :
        table [ i ] = sys.maxsize
    for i in range ( 1 , V + 1 ) :
        for j in range ( m ) :
            if ( coins [ j ] <= i ) :
                sub_res = table [ i - coins [ j ] ]
                if ( sub_res != sys.maxsize and sub_res + 1 < table [ i ] ) :
                    table [ i ] = sub_res + 1
    return table [ V ]

FIND_MINIMUM_RADIUS_ATLEAST_K_POINT_LIE_INSIDE_CIRCLE | def minRadius ( k , x , y , n ) :
    dis = [ 0 ] * n
    for i in range ( 0 , n ) :
        dis [ i ] = x [ i ] * x [ i ] + y [ i ] * y [ i ]
    dis.sort ( )
    return dis [ k - 1 ]

FIND_MIRROR_IMAGE_POINT_2_D_PLANE | def mirrorImage ( a , b , c , x1 , y1 ) :
    temp = - 2 * ( a * x1 + b * y1 + c ) / ( a * a + b * b )
    x = temp * a + x1
    y = temp * b + y1
    return ( x , y )

FIND_NUMBER_ENDLESS_POINTS | def countEndless ( input_mat , n ) :
    row = np.zeros ( ( n , n ) )
    col = np.zeros ( ( n , n ) )
    for j in range ( n ) :
        isEndless = 1
        for i in range ( n - 1 , - 1 , - 1 ) :
            if ( input_mat [ i ] [ j ] == 0 ) :
                isEndless = 0
            col [ i ] [ j ] = isEndless
    for i in range ( n ) :
        isEndless = 1
        for j in range ( n - 1 , - 1 , - 1 ) :
            if ( input_mat [ i ] [ j ] == 0 ) :
                isEndless = 0
            row [ i ] [ j ] = isEndless
    ans = 0
    for i in range ( n ) :
        for j in range ( 1 , n ) :
            if ( row [ i ] [ j ] and col [ i ] [ j ] ) :
                ans += 1
    return ans

FIND_NUMBER_PERFECT_SQUARES_TWO_GIVEN_NUMBERS | def CountSquares ( a , b ) :
    cnt = 0
    for i in range ( a , b + 1 ) :
        j = 1 ;
        while j * j <= i :
            if j * j == i :
                cnt = cnt + 1
            j = j + 1
        i = i + 1
    return cnt

FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING_1 | def count ( a , b ) :
    m = len ( a )
    n = len ( b )
    lookup = [ [ 0 ] * ( n + 1 ) for i in range ( m + 1 ) ]
    for i in range ( n + 1 ) :
        lookup [ 0 ] [ i ] = 0
    for i in range ( m + 1 ) :
        lookup [ i ] [ 0 ] = 1
    for i in range ( 1 , m + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if a [ i - 1 ] == b [ j - 1 ] :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j - 1 ] + lookup [ i - 1 ] [ j ]
            else :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j ]
    return lookup [ m ] [ n ]

FIND_NUMBER_TRANSFORMATION_MAKE_TWO_MATRIX_EQUAL | def countOps ( A , B , m , n ) :
    for i in range ( n ) :
        for j in range ( m ) :
            A [ i ] [ j ] -= B [ i ] [ j ]
    for i in range ( 1 , n ) :
        for j in range ( 1 , n ) :
            if ( A [ i ] [ j ] - A [ i ] [ 0 ] - A [ 0 ] [ j ] + A [ 0 ] [ 0 ] != 0 ) :
                return - 1
    result = 0
    for i in range ( n ) :
        result += abs ( A [ i ] [ 0 ] )
    for j in range ( m ) :
        result += abs ( A [ 0 ] [ j ] - A [ 0 ] [ 0 ] )
    return ( result )

FIND_N_TH_ELEMENT_FROM_STERNS_DIATOMIC_SERIES | def findSDSFunc ( n ) :
    DP = [ 0 ] * ( n + 1 )
    DP [ 0 ] = 0
    DP [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        if ( int ( i % 2 ) == 0 ) :
            DP [ i ] = DP [ int ( i / 2 ) ]
        else :
            DP [ i ] = ( DP [ int ( ( i - 1 ) / 2 ) ] + DP [ int ( ( i + 1 ) / 2 ) ] )
    return DP [ n ]

FIND_ONE_EXTRA_CHARACTER_STRING_1 | def findExtraCharcter ( strA , strB ) :
    res = 0
    for i in range ( 0 , len ( strA ) ) :
        res = res ^ ( ord ) ( strA [ i ] )
    for i in range ( 0 , len ( strB ) ) :
        res = res ^ ( ord ) ( strB [ i ] )
    return ( ( chr ) ( res ) ) ;

FIND_PAIRS_GIVEN_SUM_ELEMENTS_PAIR_DIFFERENT_ROWS | def pairSum ( mat , n , sum ) :
    for i in range ( n ) :
        mat [ i ].sort ( )
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            left = 0
            right = n - 1
            while ( left < n and right >= 0 ) :
                if ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) == sum ) :
                    print ( "(" , mat [ i ] [ left ] , ", " , mat [ j ] [ right ] , "), " , end = " " )
                    left += 1
                    right -= 1
                else :
                    if ( ( mat [ i ] [ left ] + mat [ j ] [ right ] ) < sum ) :
                        left += 1
                    else :
                        right -= 1

FIND_PAIR_MAXIMUM_GCD_ARRAY | def findMaxGCD ( arr , n ) :
    high = 0
    i = 0
    while i < n :
        high = max ( high , arr [ i ] )
        i = i + 1
    divisors = [ 0 ] * ( high + 1 )
    i = 0
    while i < n :
        j = 1
        while j <= math.sqrt ( arr [ i ] ) :
            if ( arr [ i ] % j == 0 ) :
                divisors [ j ] = divisors [ j ] + 1
                if ( j != arr [ i ] / j ) :
                    divisors [ arr [ i ] / j ] = divisors [ arr [ i ] / j ] + 1
            j = j + 1
        i = i + 1
    i = high
    while i >= 1 :
        if ( divisors [ i ] > 1 ) :
            return i
        i = i - 1
    return 1

FIND_PAIR_MAXIMUM_GCD_ARRAY_1 | def findMaxGCD ( arr , n ) :
    high = 0
    for i in range ( 0 , n ) :
        high = max ( high , arr [ i ] )
    count = [ 0 ] * ( high + 1 )
    for i in range ( 0 , n ) :
        count [ arr [ i ] ] += 1
    counter = 0
    for i in range ( high , 0 , - 1 ) :
        j = i
        while ( j <= high ) :
            if ( count [ j ] > 0 ) :
                counter += count [ j ]
            j += i
            if ( counter == 2 ) :
                return i
        counter = 0
    return 1


FIND_PAIR_WITH_GREATEST_PRODUCT_IN_ARRAY | def findGreatest ( arr , n ) :
    result = - 1
    for i in range ( n ) :
        for j in range ( n - 1 ) :
            for k in range ( j + 1 , n ) :
                if ( arr [ j ] * arr [ k ] == arr [ i ] ) :
                    result = max ( result , arr [ i ] )
    return result

FIND_PATTERNS_101_GIVEN_STRING | def patternCount ( str ) :
    last = str [ 0 ]
    i = 1
    counter = 0
    while ( i < len ( str ) ) :
        if ( str [ i ] == '0' and last == '1' ) :
            while ( str [ i ] == '0' ) :
                i += 1
                if ( str [ i ] == '1' ) :
                    counter += 1
        last = str [ i ]
        i += 1
    return counter

FIND_POSITION_GIVEN_NUMBER_AMONG_NUMBERS_MADE_4_7 | def findpos ( n ) :
    i = 0
    j = len ( n )
    pos = 0
    while ( i < j ) :
        if ( n [ i ] == '4' ) :
            pos = pos * 2 + 1
        if ( n [ i ] == '7' ) :
            pos = pos * 2 + 2
        i = i + 1
    return pos

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1 | def isRectangle ( m ) :
    rows = len ( m )
    if ( rows == 0 ) :
        return False
    columns = len ( m [ 0 ] )
    for y1 in range ( rows ) :
        for x1 in range ( columns ) :
            if ( m [ y1 ] [ x1 ] == 1 ) :
                for y2 in range ( y1 + 1 , rows ) :
                    for x2 in range ( x1 + 1 , columns ) :
                        if ( m [ y1 ] [ x2 ] == 1 and m [ y2 ] [ x1 ] == 1 and m [ y2 ] [ x2 ] == 1 ) :
                            return True
    return False

FIND_RECTANGLE_BINARY_MATRIX_CORNERS_1_1 | def isRectangle ( matrix ) :
    rows = len ( matrix )
    if ( rows == 0 ) :
        return False
    columns = len ( matrix [ 0 ] )
    table = { }
    for i in range ( rows ) :
        for j in range ( columns - 1 ) :
            for k in range ( j + 1 , columns ) :
                if ( matrix [ i ] [ j ] == 1 and matrix [ i ] [ k ] == 1 ) :
                    if ( j in table and k in table [ j ] ) :
                        return True
                    if ( k in table and j in table [ k ] ) :
                        return True
                    if j not in table :
                        table [ j ] = set ( )
                    if k not in table :
                        table [ k ] = set ( )
                    table [ j ].add ( k )
                    table [ k ].add ( j )
    return False

FIND_REPEATING_ELEMENT_SORTED_ARRAY_SIZE_N | def findRepeatingElement ( arr , low , high ) :
    if low > high :
        return - 1
    mid = int ( ( low + high ) / 2 )
    if ( arr [ mid ] != mid + 1 ) :
        if ( mid > 0 and arr [ mid ] == arr [ mid - 1 ] ) :
            return mid
        return findRepeatingElement ( arr , low , mid - 1 )
    return findRepeatingElement ( arr , mid + 1 , high )

FIND_REPETITIVE_ELEMENT_1_N_1 | def findRepeating ( arr , n ) :
    return sum ( arr [ : n ] ) - ( ( ( n - 1 ) * n ) // 2 )

FIND_REPETITIVE_ELEMENT_1_N_1_1 | def findRepeating ( arr , n ) :
    s = set ( )
    for i in range ( n ) :
        if arr [ i ] in s :
            return arr [ i ]
        s.add ( arr [ i ] )
    rteurn - 1

FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY_1 | def countRotations ( arr , low , high ) :
    if ( high < low ) :
        return 0
    if ( high == low ) :
        return low
    mid = low + ( high - low ) / 2
    mid = int ( mid )
    if ( mid < high and arr [ mid + 1 ] < arr [ mid ] ) :
        return ( mid + 1 )
    if ( mid > low and arr [ mid ] < arr [ mid - 1 ] ) :
        return mid
    if ( arr [ high ] > arr [ mid ] ) :
        return countRotations ( arr , low , mid - 1 )
    return countRotations ( arr , mid + 1 , high )

FIND_SUBARRAY_WITH_GIVEN_SUM | def subArraySum ( arr , n , sum ) :
    for i in range ( n ) :
        curr_sum = arr [ i ]
        j = i + 1
        while j <= n :
            if curr_sum == sum :
                print ( "Sum found between" )
                print ( "indexes %d and %d" % ( i , j - 1 ) )
                return 1
            if curr_sum > sum or j == n :
                break
            curr_sum = curr_sum + arr [ j ]
            j += 1
    print ( "No subarray found" )
    return 0

FIND_SUBARRAY_WITH_GIVEN_SUM_1 | def subArraySum ( arr , n , sum ) :
    curr_sum = arr [ 0 ]
    start = 0
    i = 1
    while i <= n :
        while curr_sum > sum and start < i - 1 :
            curr_sum = curr_sum - arr [ start ]
            start += 1
        if curr_sum == sum :
            print ( "Sum found between indexes" )
            print ( "%d and %d" % ( start , i - 1 ) )
            return 1
        if i < n :
            curr_sum = curr_sum + arr [ i ]
        i += 1
    print ( "No subarray found" )
    return 0

FIND_SUM_EVEN_FACTORS_NUMBER | def sumofFactors ( n ) :
    if ( n % 2 != 0 ) :
        return 0
    res = 1
    for i in range ( 2 , ( int ) ( math.sqrt ( n ) ) + 1 ) :
        count = 0
        curr_sum = 1
        curr_term = 1
        while ( n % i == 0 ) :
            count = count + 1
            n = n // i
            if ( i == 2 and count == 1 ) :
                curr_sum = 0
            curr_term = curr_term * i
            curr_sum = curr_sum + curr_term
        res = res * curr_sum
    if ( n >= 2 ) :
        res = res * ( 1 + n )
    return res

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS | def evenSum ( n ) :
    C = [ [ 0 for x in range ( n + 1 ) ] for y in range ( n + 1 ) ]
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , min ( i , n ) + 1 ) :
            if j == 0 or j == i :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    sum = 0 ;
    for i in range ( 0 , n + 1 ) :
        if i % 2 == 0 :
            sum = sum + C [ n ] [ i ]
    return sum

FIND_SUM_EVEN_INDEX_BINOMIAL_COEFFICIENTS_1 | def evenbinomialCoeffSum ( n ) :
    return ( 1 << ( n - 1 ) )

FIND_SUM_MODULO_K_FIRST_N_NATURAL_NUMBER | def findSum ( N , K ) :
    ans = 0
    for i in range ( 1 , N + 1 ) :
        ans += ( i % K )
    return ans

FIND_SUM_NODES_GIVEN_PERFECT_BINARY_TREE_1 | def sumNodes ( l ) :
    leafNodeCount = math.pow ( 2 , l - 1 )
    sumLastLevel = 0
    sumLastLevel = ( ( leafNodeCount * ( leafNodeCount + 1 ) ) / 2 )
    sum = sumLastLevel * l
    return sum

FIND_SUM_ODD_FACTORS_NUMBER | def sumofoddFactors ( n ) :
    res = 1
    while n % 2 == 0 :
        n = n // 2
    for i in range ( 3 , int ( math.sqrt ( n ) + 1 ) ) :
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0 :
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2 :
        res *= ( 1 + n )
    return res

FIND_SUM_UNIQUE_SUB_ARRAY_SUM_GIVEN_ARRAY | def findSubarraySum ( arr , n ) :
    res = 0
    m = dict ( )
    for i in range ( n ) :
        Sum = 0
        for j in range ( i , n ) :
            Sum += arr [ j ]
            m [ Sum ] = m.get ( Sum , 0 ) + 1
    for x in m :
        if m [ x ] == 1 :
            res += x
    return res

FIND_THE_ELEMENT_BEFORE_WHICH_ALL_THE_ELEMENTS_ARE_SMALLER_THAN_IT_AND_AFTER_WHICH_ALL_ARE_GREATER_THAN_IT | def findElement ( arr , n ) :
    leftMax = [ None ] * n
    leftMax [ 0 ] = float ( '-inf' )
    for i in range ( 1 , n ) :
        leftMax [ i ] = max ( leftMax [ i - 1 ] , arr [ i - 1 ] )
    rightMin = float ( 'inf' )
    for i in range ( n - 1 , - 1 , - 1 ) :
        if leftMax [ i ] < arr [ i ] and rightMin > arr [ i ] :
            return i
        rightMin = min ( rightMin , arr [ i ] )
    return - 1

FIND_THE_ELEMENT_THAT_APPEARS_ONCE | def getSingle ( arr , n ) :
    ones = 0
    twos = 0
    for i in range ( n ) :
        twos = twos | ( ones & arr [ i ] )
        ones = ones ^ arr [ i ]
        common_bit_mask = ~ ( ones & twos )
        ones &= common_bit_mask
        twos &= common_bit_mask
    return ones

FIND_THE_ELEMENT_THAT_APPEARS_ONCE_2 | def singleNumber ( nums , n ) :
    return ( 3 * sum ( set ( nums ) ) - sum ( nums ) ) / 2

FIND_THE_FIRST_MISSING_NUMBER | def findFirstMissing ( array , start , end ) :
    if ( start > end ) :
        return end + 1
    if ( start != array [ start ] ) :
        return start
    mid = int ( ( start + end ) / 2 )
    if ( array [ mid ] == mid ) :
        return findFirstMissing ( array , mid + 1 , end )
    return findFirstMissing ( array , start , mid )

FIND_THE_LARGEST_SUBARRAY_WITH_0_SUM | def maxLen ( arr , n ) :
    max_len = 0
    for i in range ( n ) :
        curr_sum = 0
        for j in range ( i , n ) :
            curr_sum += arr [ j ]
            if curr_sum == 0 :
                max_len = max ( max_len , j - i + 1 )
    return max_len


FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING | def findMaximum ( arr , low , high ) :
    max = arr[low]
    for i in range(low, high + 1):
        if arr[i] > max:
            max = arr[i]
    return max

FIND_THE_MAXIMUM_SUBARRAY_XOR_IN_A_GIVEN_ARRAY | def maxSubarrayXOR ( arr , n ) :
    ans = - 2147483648
    for i in range ( n ) :
        curr_xor = 0
        for j in range ( i , n ) :
            curr_xor = curr_xor ^ arr [ j ]
            ans = max ( ans , curr_xor )
    return ans

FIND_THE_MINIMUM_DISTANCE_BETWEEN_TWO_NUMBERS | def minDist ( arr , n , x , y ) :
    min_dist = 2147483647
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if ( x == arr [ i ] and y == arr [ j ] or y == arr [ i ] and x == arr [ j ] ) and min_dist > abs ( i - j ) :
                min_dist = abs ( i - j )
    return min_dist



FIND_THE_MISSING_NUMBER_1 | def getMissingNo ( a , n ) :
    i , total = 0 , 1
    for i in range ( 2 , n + 2 ) :
        total += i
        total -= a [ i - 2 ]
    return total

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES | def getOddOccurrence ( arr , arr_size ) :
    for i in range ( 0 , arr_size ) :
        count = 0
        for j in range ( 0 , arr_size ) :
            if arr [ i ] == arr [ j ] :
                count += 1
        if ( count % 2 != 0 ) :
            return arr [ i ]
    return - 1

FIND_THE_NUMBER_OCCURRING_ODD_NUMBER_OF_TIMES_2 | def getOddOccurrence ( ar , ar_size) :
    res = 0
    for i in range ( 0, ar_size ) :
        res = res ^ ar [ i ]
    return res


FIND_THREE_ELEMENT_FROM_DIFFERENT_THREE_ARRAYS_SUCH_THAT_THAT_A_B_C_K_1 | def findTriplet ( a1 , a2 , a3 , n1 , n2 , n3 , sum ) :
    s = set ( )
    for i in range ( n1 ) :
        s.add ( a1 [ i ] )
    for i in range ( n2 ) :
        for j in range ( n3 ) :
            if sum - a2 [ i ] - a3 [ j ] in s :
                return True
    return False

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO_1 | def findTriplets ( arr , n ) :
    found = False
    for i in range ( n - 1 ) :
        s = set ( )
        for j in range ( i + 1 , n ) :
            x = - ( arr [ i ] + arr [ j ] )
            if x in s :
                print ( x , arr [ i ] , arr [ j ] )
                found = True
            else :
                s.add ( arr [ j ] )
    if found == False :
        print ( "No Triplet Found" )

FIND_TRIPLETS_ARRAY_WHOSE_SUM_EQUAL_ZERO_2 | def findTriplets ( arr , n ) :
    found = False
    arr.sort ( )
    for i in range ( 0 , n - 1 ) :
        l = i + 1
        r = n - 1
        x = arr [ i ]
        while ( l < r ) :
            if ( x + arr [ l ] + arr [ r ] == 0 ) :
                print ( x , arr [ l ] , arr [ r ] )
                l += 1
                r -= 1
                found = True
            elif ( x + arr [ l ] + arr [ r ] < 0 ) :
                l += 1
            else :
                r -= 1
    if ( found == False ) :
        print ( " No Triplet Found" )

FIND_VALUE_OF_Y_MOD_2_RAISED_TO_POWER_X | def yMod ( y , x ) :
    return ( y % pow ( 2 , x ) )

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT | def isPowerOfFour ( n ) :
    if ( n == 0 ) :
        return False
    while ( n != 1 ) :
        if ( n % 4 != 0 ) :
            return False
        n = n // 4
    return True

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_1 | def isPowerOfFour ( n ) :
    count = 0
    if ( n and ( not ( n & ( n - 1 ) ) ) ) :
        while ( n > 1 ) :
            n >>= 1
            count += 1
        if ( count % 2 == 0 ) :
            return True
        else :
            return False
    return False

FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT_2 | def isPowerOfFour ( n ) :
    return ( n != 0 and ( ( n & ( n - 1 ) ) == 0 ) and not ( n & 0xAAAAAAAA ) )

FIND_WHETHER_GIVEN_INTEGER_POWER_3_NOT | def check ( n ) :
    return 1162261467 % n == 0

FIRST_ELEMENT_OCCURRING_K_TIMES_ARRAY | def firstElement ( arr , n , k ) :
    count_map = { }
    for i in range ( 0 , n ) :
        if ( arr [ i ] in count_map.keys ( ) ) :
            count_map [ arr [ i ] ] += 1
        else :
            count_map [ arr [ i ] ] = 1
        i += 1
    for i in range ( 0 , n ) :
        if ( count_map [ arr [ i ] ] == k ) :
            return arr [ i ]
        i += 1
    return - 1

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE | def first ( str ) :
    for i in range ( 0 , len ( str ) ) :
        if ( str [ i ].istitle ( ) ) :
            return str [ i ]
    return 0

FIRST_UPPERCASE_LETTER_IN_A_STRING_ITERATIVE_AND_RECURSIVE_1 | def first ( str , i ) :
    if ( str [ i ] == '\0' ) :
        return 0
    if ( str [ i ].isupper ( ) ) :
        return str [ i ]
    return first ( str , i + 1 )

FLOOR_IN_A_SORTED_ARRAY | def floorSearch ( arr , n , x ) :
    if x >= arr [ n - 1 ]: return n - 1
    if x < arr [ 0 ]: return - 1
    for i in range ( 1, n ):
        if arr [ i ] > x: return i - 1
    return - 1

FORM_MINIMUM_NUMBER_FROM_GIVEN_SEQUENCE_1 | def getMinNumberForPattern ( seq ) :
    n = len ( seq )
    if ( n >= 9 ) :
        return "-1"
    result = [ None ] * ( n + 1 )
    count = 1
    for i in range ( n + 1 ) :
        if ( i == n or seq [ i ] == 'I' ) :
            for j in range ( i - 1 , - 2 , - 1 ) :
                result [ j + 1 ] = int ( '0' + str ( count ) )
                count += 1
                if ( j >= 0 and seq [ j ] == 'I' ) :
                    break
    return result

FREQUENT_ELEMENT_ARRAY_1 | def mostFrequent ( arr , n ) :
    Hash = dict ( )
    for i in range ( n ) :
        if arr [ i ] in Hash.keys ( ) :
            Hash [ arr [ i ] ] += 1
        else :
            Hash [ arr [ i ] ] = 1
    max_count = 0
    res = - 1
    for i in Hash :
        if ( max_count < Hash [ i ] ) :
            res = i
            max_count = Hash [ i ]
    return res

FRIENDS_PAIRING_PROBLEM | def countFriendsPairings ( n ) :
    dp = [ 0 for i in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        if ( i <= 2 ) :
            dp [ i ] = i
        else :
            dp [ i ] = dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ]
    return dp [ n ]

FRIENDS_PAIRING_PROBLEM_2 | def countFriendsPairings ( n ) :
    a , b , c = 1 , 2 , 0
    if ( n <= 2 ) :
        return n
    for i in range ( 3 , n + 1 ) :
        c = b + ( i - 1 ) * a
        a = b
        b = c
    return c

GCD_ELEMENTS_GIVEN_RANGE | def rangeGCD ( n , m ) :
    return n if ( n == m ) else 1

GIVEN_A_SORTED_AND_ROTATED_ARRAY_FIND_IF_THERE_IS_A_PAIR_WITH_A_GIVEN_SUM_1 | def getMinNumberForPattern ( seq ) :
    n = len ( seq )
    if ( n >= 9 ) :
        return "-1"
    result = [ None ] * ( n + 1 )
    count = 1
    for i in range ( n + 1 ) :
        if ( i == n or seq [ i ] == 'I' ) :
            for j in range ( i - 1 , - 2 , - 1 ) :
                result [ j + 1 ] = int ( '0' + str ( count ) )
                count += 1
                if ( j >= 0 and seq [ j ] == 'I' ) :
                    break
    return "".join(str(i) for i in result)

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8 | def isSubSeqDivisible ( str ) :
    l = len ( str )
    arr = [ 0 ] * l
    for i in range ( 0 , l ) :
        for j in range ( i , l ) :
            for k in range ( j , l ) :
                if ( arr [ i ] % 8 == 0 ) :
                    return True
                elif ( ( arr [ i ] * 10 + arr [ j ] ) % 8 == 0 and i != j ) :
                    return True
                elif ( ( arr [ i ] * 100 + arr [ j ] * 10 + arr [ k ] ) % 8 == 0 and i != j and j != k and i != k ) :
                    return True
    return False

GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8_1 | def isSubSeqDivisible ( str ) :
    n = len ( str )
    dp = [ [ 0 for i in range ( 10 ) ] for i in range ( n + 1 ) ]
    arr = [ 0 for i in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        arr [ i ] = int ( str [ i - 1 ] )
    for i in range ( 1 , n + 1 ) :
        dp [ i ] [ arr [ i ] % 8 ] = 1
        for j in range ( 8 ) :
            if ( dp [ i - 1 ] [ j ] > dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 ] ) :
                dp [ i ] [ ( j * 10 + arr [ i ] ) % 8 ] = dp [ i - 1 ] [ j ]
            if ( dp [ i - 1 ] [ j ] > dp [ i ] [ j ] ) :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j ]
    for i in range ( 1 , n + 1 ) :
        if ( dp [ i ] [ 0 ] == 1 ) :
            return True
    return False

GIVEN_P_AND_N_FIND_THE_LARGEST_X_SUCH_THAT_PX_DIVIDES_N_2 | def largestPower ( n , p ) :
    x = 0
    while n :
        n /= p
        x += n
    return x

GIVEN_TWO_STRINGS_FIND_FIRST_STRING_SUBSEQUENCE_SECOND | def isSubSequence ( str1 , str2 , m , n ) :
    if m == 0 : return True
    if n == 0 : return False
    if str1 [ m - 1 ] == str2 [ n - 1 ] :
        return isSubSequence ( str1 , str2 , m - 1 , n - 1 )
    return isSubSequence ( str1 , str2 , m , n - 1 )

GNOME_SORT_A_STUPID_ONE | def gnomeSort ( arr , n ) :
    index = 0
    while index < n :
        if index == 0 :
            index = index + 1
        if arr [ index ] >= arr [ index - 1 ] :
            index = index + 1
        else :
            arr [ index ] , arr [ index - 1 ] = arr [ index - 1 ] , arr [ index ]
            index = index - 1
    return arr

HARDY_RAMANUJAN_THEOREM | def exactPrimeFactorCount ( n ) :
    count = 0
    if ( n % 2 == 0 ) :
        count = count + 1
        while ( n % 2 == 0 ) :
            n = int ( n / 2 )
    i = 3
    while ( i <= int ( math.sqrt ( n ) ) ) :
        if ( n % i == 0 ) :
            count = count + 1
            while ( n % i == 0 ) :
                n = int ( n / i )
        i = i + 2
    if ( n > 2 ) :
        count = count + 1
    return count

HEIGHT_COMPLETE_BINARY_TREE_HEAP_N_NODES | def height ( N ) :
    return math.ceil ( math.log2 ( N + 1 ) ) - 1

HEXAGONAL_NUMBER | def hexagonalNum ( n ) :
    return n * ( 2 * n - 1 )

HIGHWAY_BILLBOARD_PROBLEM | def maxRevenue ( m , x , revenue , n , t ) :
    maxRev = [ 0 ] * ( m + 1 )
    nxtbb = 0
    for i in range ( 1 , m + 1 ) :
        if ( nxtbb < n ) :
            if ( x [ nxtbb ] != i ) :
                maxRev [ i ] = maxRev [ i - 1 ]
            else :
                if ( i <= t ) :
                    maxRev [ i ] = max ( maxRev [ i - 1 ] , revenue [ nxtbb ] )
                else :
                    maxRev [ i ] = max ( maxRev [ i - t - 1 ] + revenue [ nxtbb ] , maxRev [ i - 1 ] )
                nxtbb += 1
        else :
            maxRev [ i ] = maxRev [ i - 1 ]
    return maxRev [ m ]

HORNERS_METHOD_POLYNOMIAL_EVALUATION | def horner ( poly , n , x ) :
    result = poly [ 0 ]
    for i in range ( 1 , n ) :
        result = result * x + poly [ i ]
    return result

HOW_CAN_WE_SUM_THE_DIGITS_OF_A_GIVEN_NUMBER_IN_SINGLE_STATEMENT | def getSum ( n ) :
    sum = 0
    while ( n != 0 ) :
        sum = sum + int ( n % 10 )
        n = int ( n / 10 )
    return sum

HOW_TO_AVOID_OVERFLOW_IN_MODULAR_MULTIPLICATION | def mulmod ( a , b , mod ) :
    res = 0
    a = a % mod
    while ( b > 0 ) :
        if ( b % 2 == 1 ) :
            res = ( res + a ) % mod
        a = ( a * 2 ) % mod
        b //= 2
    return res % mod

HOW_TO_BEGIN_WITH_COMPETITIVE_PROGRAMMING | def search ( arr , x ) :
    n = len ( arr )
    for j in range ( 0 , n ) :
        if ( x == arr [ j ] ) :
            return j
    return - 1

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP | def isHeap ( arr , i , n ) :
    if i > int ( ( n - 2 ) / 2 ) :
        return True
    if ( arr [ i ] >= arr [ 2 * i + 1 ] and arr [ i ] >= arr [ 2 * i + 2 ] and isHeap ( arr , 2 * i + 1 , n ) and isHeap ( arr , 2 * i + 2 , n ) ) :
        return True
    return False

HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP_1 | def isHeap ( arr , n ) :
    for i in range ( int ( ( n - 2 ) / 2 ) + 1 ) :
        if arr [ 2 * i + 1 ] > arr [ i ] :
            return False
        if ( 2 * i + 2 < n and arr [ 2 * i + 2 ] > arr [ i ] ) :
            return False
    return True

HOW_TO_PRINT_MAXIMUM_NUMBER_OF_A_USING_GIVEN_FOUR_KEYS | def search ( arr , n , x ) :
    for j in range ( 0 , n ) :
        if ( x == arr [ j ] ) :
            return j
    return - 1

HOW_TO_TURN_OFF_A_PARTICULAR_BIT_IN_A_NUMBER | def turnOffK ( n , k ) :
    if ( k <= 0 ) :
        return n
    return ( n & ~ ( 1 << ( k - 1 ) ) )

HYPERCUBE_GRAPH | def power ( n ) :
    if n == 1 :
        return 2
    return 2 * power ( n - 1 )

INTEGER_POSITIVE_VALUE_POSITIVE_NEGATIVE_VALUE_ARRAY | def findInteger ( arr , n ) :
    hash = dict ( )
    maximum = 0
    for i in arr :
        if ( i < 0 ) :
            if abs ( i ) not in hash.keys ( ) :
                hash [ abs ( i ) ] = - 1
            else :
                hash [ abs ( i ) ] -= 1
        else :
            hash [ i ] = hash.get ( i , 0 ) + 1
    for i in arr :
        if i in hash.keys ( ) and hash [ i ] > 0 :
            return i
    return - 1

K_TH_DIGIT_RAISED_POWER_B | def kthdigit ( a , b , k ) :
    p = a ** b
    count = 0
    while ( p > 0 and count < k ) :
        rem = p % 10
        count = count + 1
        if ( count == k ) :
            return rem
        p = p // 10
    return 0


K_TH_ELEMENT_TWO_SORTED_ARRAYS | def kth ( arr1 , arr2 , m , n , k ) :
    sorted1 = [ 0 ] * ( m + n )
    i = 0
    j = 0
    d = 0
    while ( i < m and j < n ) :
        if ( arr1 [ i ] < arr2 [ j ] ) :
            sorted1 [ d ] = arr1 [ i ]
            i += 1
        else :
            sorted1 [ d ] = arr2 [ j ]
            j += 1
        d += 1
    while ( i < m ) :
        sorted1 [ d ] = arr1 [ i ]
        d += 1
        i += 1
    while ( j < n ) :
        sorted1 [ d ] = arr2 [ j ]
        d += 1
        j += 1
    return sorted1 [ k - 1 ]

K_TH_LARGEST_SUM_CONTIGUOUS_SUBARRAY | def kthLargestSum ( arr , n , k ) :
    sum = [ ]
    sum.append ( 0 )
    sum.append ( arr [ 0 ] )
    for i in range ( 2 , n + 1 ) :
        sum.append ( sum [ i - 1 ] + arr [ i - 1 ] )
    Q = [ ]
    heapq.heapify ( Q )
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , n + 1 ) :
            x = sum [ j ] - sum [ i - 1 ]
            if len ( Q ) < k :
                heapq.heappush ( Q , x )
            else :
                if Q [ 0 ] < x :
                    heapq.heappop ( Q )
                    heapq.heappush ( Q , x )
    return Q [ 0 ]

K_TH_MISSING_ELEMENT_INCREASING_SEQUENCE_NOT_PRESENT_GIVEN_SEQUENCE | def find ( a , b , k , n1 , n2 ) :
    s = set ( )
    for i in range ( n2 ) :
        s.add ( b [ i ] )
    missing = 0
    for i in range ( n1 ) :
        if a [ i ] not in s :
            missing += 1
        if missing == k :
            return a [ i ]
    return - 1

K_TH_PRIME_FACTOR_GIVEN_NUMBER | def kPrimeFactor ( n , k ) :
    while ( n % 2 == 0 ) :
        k = k - 1
        n = n // 2
        if ( k == 0 ) :
            return 2
    i = 3
    while i <= math.sqrt ( n ) :
        while ( n % i == 0 ) :
            if ( k == 1 ) :
                return i
            k = k - 1
            n = n // i
        i = i + 2
    if ( n > 2 and k == 1 ) :
        return n
    return - 1

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S | def findSubArray ( arr , n ) :
    sum = 0
    maxsize = - 1
    for i in range ( 0 , n - 1 ) :
        sum = - 1 if ( arr [ i ] == 0 ) else 1
        for j in range ( i + 1 , n ) :
            sum = sum + ( - 1 ) if ( arr [ j ] == 0 ) else sum + 1
            if ( sum == 0 and maxsize < j - i + 1 ) :
                maxsize = j - i + 1
                startindex = i
    if ( maxsize == - 1 ) :
        print ( "No such subarray" )
    else :
        print ( startindex , "to" , startindex + maxsize - 1 )
    return maxsize

LARGEST_SUBARRAY_WITH_EQUAL_NUMBER_OF_0S_AND_1S_1 | def maxLen ( arr , n ) :
    hash_map = { }
    curr_sum = 0
    max_len = 0
    ending_index = - 1
    for i in range ( 0 , n ) :
        if ( arr [ i ] == 0 ) :
            arr [ i ] = - 1
        else :
            arr [ i ] = 1
    for i in range ( 0 , n ) :
        curr_sum = curr_sum + arr [ i ]
        if ( curr_sum == 0 ) :
            max_len = i + 1
            ending_index = i
        if ( curr_sum + n ) in hash_map :
            if max_len < i - hash_map [ curr_sum + n ] :
                max_len = i - hash_map [ curr_sum + n ]
                ending_index = i
        else :
            hash_map[curr_sum + n] = i
    for i in range ( 0 , n ) :
        if ( arr [ i ] == - 1 ) :
            arr [ i ] = 0
        else :
            arr [ i ] = 1
    print ( ending_index - max_len + 1 , end = " " )
    print ( "to" , end = " " )
    print ( ending_index )
    return max_len

LARGEST_SUBSEQUENCE_GCD_GREATER_1 | def largestGCDSubsequence ( arr , n ) :
    ans = 0
    maxele = max ( arr )
    for i in range ( 2 , maxele + 1 ) :
        count = 0
        for j in range ( n ) :
            if ( arr [ j ] % i == 0 ) :
                count += 1
        ans = max ( ans , count )
    return ans

LCS_FORMED_CONSECUTIVE_SEGMENTS_LEAST_LENGTH_K | def longestSubsequenceCommonSegment ( k , s1 , s2 ) :
    n = len ( s1 )
    m = len ( s2 )
    lcs = [ [ 0 for x in range ( m + 1 ) ] for y in range ( n + 1 ) ]
    cnt = [ [ 0 for x in range ( m + 1 ) ] for y in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , m + 1 ) :
            lcs [ i ] [ j ] = max ( lcs [ i - 1 ] [ j ] , lcs [ i ] [ j - 1 ] )
            if ( s1 [ i - 1 ] == s2 [ j - 1 ] ) :
                cnt [ i ] [ j ] = cnt [ i - 1 ] [ j - 1 ] + 1
            if ( cnt [ i ] [ j ] >= k ) :
                for a in range ( k , cnt [ i ] [ j ] + 1 ) :
                    lcs [ i ] [ j ] = max ( lcs [ i ] [ j ] , lcs [ i - a ] [ j - a ] + a )
    return lcs [ n ] [ m ]

LENGTH_LONGEST_BALANCED_SUBSEQUENCE | def maxLength ( s , n ) :
    dp = [ [ 0 for i in range ( n ) ] for i in range ( n ) ]
    for i in range ( n - 1 ) :
        if ( s [ i ] == '(' and s [ i + 1 ] == ')' ) :
            dp [ i ] [ i + 1 ] = 2
    for l in range ( 2 , n ) :
        i = - 1
        for j in range ( l , n ) :
            i += 1
            if ( s [ i ] == '(' and s [ j ] == ')' ) :
                dp [ i ] [ j ] = 2 + dp [ i + 1 ] [ j - 1 ]
            for k in range ( i , j ) :
                dp [ i ] [ j ] = max ( dp [ i ] [ j ] , dp [ i ] [ k ] + dp [ k + 1 ] [ j ] )
    return dp [ 0 ] [ n - 1 ]

LENGTH_LONGEST_BALANCED_SUBSEQUENCE_1 | def maxLength ( s , n ) :
    invalidOpenBraces = 0
    invalidCloseBraces = 0
    for i in range ( n ) :
        if ( s [ i ] == '(' ) :
            invalidOpenBraces += 1
        else :
            if ( invalidOpenBraces == 0 ) :
                invalidCloseBraces += 1
            else :
                invalidOpenBraces -= 1
    return ( n - ( invalidOpenBraces + invalidCloseBraces ) )

LENGTH_LONGEST_SUB_STRING_CAN_MAKE_REMOVED | def longestNull ( S ) :
    arr = [ ]
    arr.append ( [ '@' , - 1 ] )
    maxlen = 0
    for i in range ( len ( S ) ) :
        arr.append ( [ S [ i ] , i ] )
        while ( len ( arr ) >= 3 and arr [ len ( arr ) - 3 ] [ 0 ] == '1' and arr [ len ( arr ) - 2 ] [ 0 ] == '0' and arr [ len ( arr ) - 1 ] [ 0 ] == '0' ) :
            arr.pop ( )
            arr.pop ( )
            arr.pop ( )
        tmp = arr [ - 1 ]
        maxlen = max ( maxlen , i - tmp [ 1 ] )
    return maxlen

LENGTH_OF_THE_LONGEST_ARITHMATIC_PROGRESSION_IN_A_SORTED_ARRAY | def lenghtOfLongestAP ( set , n ) :
    if ( n <= 2 ) :
        return n
    L = [ [ 0 for x in range ( n ) ] for y in range ( n ) ]
    llap = 2
    for i in range ( n ) :
        L [ i ] [ n - 1 ] = 2
    for j in range ( n - 2 , 0 , - 1 ) :
        i = j - 1
        k = j + 1
        while ( i >= 0 and k <= n - 1 ) :
            if ( set [ i ] + set [ k ] < 2 * set [ j ] ) :
                k += 1
            elif ( set [ i ] + set [ k ] > 2 * set [ j ] ) :
                L [ i ] [ j ] = 2
                i -= 1
            else :
                L [ i ] [ j ] = L [ j ] [ k ] + 1
                llap = max ( llap , L [ i ] [ j ] )
                i -= 1
                k += 1
        while ( i >= 0 ) :
            L [ i ] [ j ] = 2
            i -= 1
    return llap

LEONARDO_NUMBER_1 | def leonardo ( n ) :
    dp = [ ]
    dp.append ( 1 )
    dp.append ( 1 )
    for i in range ( 2 , n + 1 ) :
        dp.append ( dp [ i - 1 ] + dp [ i - 2 ] + 1 )
    return dp [ n ]

LEXICOGRAPHICALLY_LARGEST_SUBSEQUENCE_EVERY_CHARACTER_OCCURS_LEAST_K_TIMES | def subsequence ( s , t , n , k ) :
    last = 0
    cnt = 0
    new_last = 0
    size = 0
    string = 'zyxwvutsrqponmlkjihgfedcba'
    for ch in string :
        cnt = 0
        for i in range ( last , n ) :
            if s [ i ] == ch :
                cnt += 1
        if cnt >= k :
            for i in range ( last , n ) :
                if s [ i ] == ch :
                    t [ size ] = ch
                    new_last = i
                    size += 1
            last = new_last
    t[size] = '\0';

LEXICOGRAPHICALLY_MINIMUM_STRING_ROTATION | def minLexRotation ( str_ ) :
    n = len ( str_ )
    arr = [ 0 ] * n
    concat = str_ + str_
    for i in range ( n ) :
        arr [ i ] = concat [ i : n + i ]
    arr.sort ( )
    return arr [ 0 ]

LEXICOGRAPHICALLY_NEXT_STRING | def nextWord ( s ) :
    if ( s == " " ) :
        return "a"
    i = len ( s ) - 1
    while ( s [ i ] == 'z' and i >= 0 ) :
        i -= 1
    if ( i == - 1 ) :
        s = s + 'a'
    else :
        s = s [ 0 : i ] + chr ( ord ( s [ i ] ) + 1 ) + s [ i + 1 : ]
    return s

LEXICOGRAPHICALLY_PREVIOUS_PERMUTATION_IN_C | def prevPermutation ( str ) :
    n = len ( str ) - 1
    i = n
    while ( i > 0 and str [ i - 1 ] <= str [ i ] ) :
        i -= 1
    if ( i <= 0 ) :
        return False
    j = i - 1
    while ( j + 1 <= n and str [ j + 1 ] <= str [ i - 1 ] ) :
        j += 1
    str = list ( str )
    temp = str [ i - 1 ]
    str [ i - 1 ] = str [ j ]
    str [ j ] = temp
    str = ''.join ( str )
    str [ : : - 1 ]
    return True

LEXICOGRAPHICALLY_SMALLEST_ARRAY_K_CONSECUTIVE_SWAPS | def minimizeWithKSwaps ( arr , n , k ) :
    for i in range ( n - 1 ) :
        pos = i
        for j in range ( i + 1 , n ) :
            if ( j - i > k ) :
                break
            if ( arr [ j ] < arr [ pos ] ) :
                pos = j
        for j in range ( pos , i , - 1 ) :
            arr [ j ] , arr [ j - 1 ] = arr [ j - 1 ] , arr [ j ]
        k -= pos - i

LEXICOGRAPHICAL_CONCATENATION_SUBSTRINGS_STRING | def lexicographicSubConcat ( s ) :
    n = len ( s )
    sub_count = ( n * ( n + 1 ) ) // 2
    arr = [ 0 ] * sub_count
    index = 0
    for i in range ( n ) :
        for j in range ( 1 , n - i + 1 ) :
            arr [ index ] = s [ i : i + j ]
            index += 1
    arr.sort ( )
    res = ""
    for i in range ( sub_count ) :
        res += arr [ i ]
    return res

LONGEST_COMMON_SUBSEQUENCE_WITH_AT_MOST_K_CHANGES_ALLOWED | def lcs ( dp , arr1 , n , arr2 , m , k ) :
    if k < 0 :
        return - ( 10 ** 7 )
    if n < 0 or m < 0 :
        return 0
    ans = dp [ n ] [ m ] [ k ]
    if ans != - 1 :
        return ans
    ans = max ( lcs ( dp , arr1 , n - 1 , arr2 , m , k ) , lcs ( dp , arr1 , n , arr2 , m - 1 , k ) )
    if arr1 [ n - 1 ] == arr2 [ m - 1 ] :
        ans = max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k ) )
    ans = max ( ans , lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k - 1 ) )
    return ans

LONGEST_COMMON_SUBSTRING | def LCSubStr ( X , Y , m , n ) :
    LCSuff = [ [ 0 for k in range ( n + 1 ) ] for l in range ( m + 1 ) ]
    result = 0
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if ( i == 0 or j == 0 ) :
                LCSuff [ i ] [ j ] = 0
            elif ( X [ i - 1 ] == Y [ j - 1 ] ) :
                LCSuff [ i ] [ j ] = LCSuff [ i - 1 ] [ j - 1 ] + 1
                result = max ( result , LCSuff [ i ] [ j ] )
            else :
                LCSuff [ i ] [ j ] = 0
    return result

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF | def findLength ( str ) :
    n = len ( str )
    maxlen = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n , 2 ) :
            length = j - i + 1
            leftsum = 0
            rightsum = 0
            for k in range ( 0 , int ( length / 2 ) ) :
                leftsum += ( int ( str [ i + k ] ) - int ( '0' ) )
                rightsum += ( int ( str [ i + k + int ( length / 2 ) ] ) - int ( '0' ) )
            if ( leftsum == rightsum and maxlen < length ) :
                maxlen = length
    return maxlen

LONGEST_EVEN_LENGTH_SUBSTRING_SUM_FIRST_SECOND_HALF_1 | def findLength ( string ) :
    n = len ( string )
    maxlen = 0
    Sum = [ [ 0 for x in range ( n ) ] for y in range ( n ) ]
    for i in range ( 0 , n ) :
        Sum [ i ] [ i ] = int ( string [ i ] )
    for length in range ( 2 , n + 1 ) :
        for i in range ( 0 , n - length + 1 ) :
            j = i + length - 1
            k = length // 2
            Sum [ i ] [ j ] = ( Sum [ i ] [ j - k ] + Sum [ j - k + 1 ] [ j ] )
            if ( length % 2 == 0 and Sum [ i ] [ j - k ] == Sum [ ( j - k + 1 ) ] [ j ] and length > maxlen ) :
                maxlen = length
    return maxlen

LONGEST_INCREASING_ODD_EVEN_SUBSEQUENCE | def longOddEvenIncSeq ( arr , n ) :
    lioes = list ( )
    maxLen = 0
    for i in range ( n ) :
        lioes.append ( 1 )
    i = 1
    for i in range ( n ) :
        for j in range ( i ) :
            if ( arr [ i ] > arr [ j ] and ( arr [ i ] + arr [ j ] ) % 2 != 0 and lioes [ i ] < lioes [ j ] + 1 ) :
                lioes [ i ] = lioes [ j ] + 1
    for i in range ( n ) :
        if maxLen < lioes [ i ] :
            maxLen = lioes [ i ]
    return maxLen

LONGEST_INCREASING_SUBSEQUENCE_1 | def lis ( arr , n ) :
    lis = [ 1 ] * n
    for i in range ( 1 , n ) :
        for j in range ( 0 , i ) :
            if arr [ i ] > arr [ j ] and lis [ i ] < lis [ j ] + 1 :
                lis [ i ] = lis [ j ] + 1
    maximum = 0
    for i in range ( n ) :
        maximum = max ( maximum , lis [ i ] )
    return maximum

LONGEST_PREFIX_ALSO_SUFFIX_1 | def longestPrefixSuffix ( s ) :
    n = len ( s )
    lps = [ 0 ] * n
    l = 0
    i = 1
    while ( i < n ) :
        if ( s [ i ] == s [ l ] ) :
            l = l + 1
            lps [ i ] = l
            i = i + 1
        else :
            if ( l != 0 ) :
                l = lps [ l - 1 ]
            else :
                lps [ i ] = 0
                i = i + 1
    res = lps [ n - 1 ]
    if ( res > n / 2 ) :
        return n // 2
    else :
        return res

LONGEST_REPEATED_SUBSEQUENCE_1 | def longestRepeatedSubSeq ( str ) :
    n = len ( str )
    dp = [ [ 0 for i in range ( n + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if ( str [ i - 1 ] == str [ j - 1 ] and i != j ) :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    res = ''
    i = n
    j = n
    while ( i > 0 and j > 0 ) :
        if ( dp [ i ] [ j ] == dp [ i - 1 ] [ j - 1 ] + 1 ) :
            res += str [ i - 1 ]
            i -= 1
            j -= 1
        elif ( dp [ i ] [ j ] == dp [ i - 1 ] [ j ] ) :
            i -= 1
        else :
            j -= 1
    res = ''.join ( reversed ( res ) )
    return res

LONGEST_REPEATING_SUBSEQUENCE | def findLongestRepeatingSubSeq ( str ) :
    n = len ( str )
    dp = [ [ 0 ] * ( n + 1 ) ] * ( n + 1 )
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if ( str [ i - 1 ] == str [ j - 1 ] and i != j ) :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    return dp [ n ] [ n ]

LONGEST_SUBARRAY_COUNT_1S_ONE_COUNT_0S | def lenOfLongSubarr ( arr , n ) :
    um = { }
    sum = 0
    maxLen = 0
    for i in range ( n ) :
        if arr [ i ] == 0 :
            sum += - 1
        else :
            sum += 1
        if ( sum == 1 ) :
            maxLen = i + 1
        elif ( sum not in um ) :
            um [ sum ] = i
        if ( ( sum - 1 ) in um ) :
            if ( maxLen < ( i - um [ sum - 1 ] ) ) :
                maxLen = i - um [ sum - 1 ]
    return maxLen

LONGEST_SUBARRAY_SUM_DIVISIBLE_K | def longSubarrWthSumDivByK ( arr , n , k ) :
    um = { }
    mod_arr = [ 0 for i in range ( n ) ]
    max = 0
    curr_sum = 0
    for i in range ( n ) :
        curr_sum += arr [ i ]
        mod_arr [ i ] = ( ( curr_sum % k ) + k ) % k
    for i in range ( n ) :
        if ( mod_arr [ i ] == 0 ) :
            max = i + 1
        elif ( mod_arr [ i ] in um ) :
            um [ mod_arr [ i ] ] = i
        else :
            if ( max < ( i - um [ mod_arr [ i ] ] ) ) :
                max = i - um [ mod_arr [ i ] ]
    return max

LONGEST_SUBSEQUENCE_DIFFERENCE_ADJACENTS_ONE_SET_2 | def longLenSub ( arr , n ) :
    um = defaultdict ( lambda : 0 )
    longLen = 0
    for i in range ( n ) :
        len1 = 0
        if ( arr [ i - 1 ] in um and len1 < um [ arr [ i ] - 1 ] ) :
            len1 = um [ arr [ i ] - 1 ]
        if ( arr [ i ] + 1 in um and len1 < um [ arr [ i ] + 1 ] ) :
            len1 = um [ arr [ i ] + 1 ]
        um [ arr [ i ] ] = len1 + 1
        if longLen < um [ arr [ i ] ] :
            longLen = um [ arr [ i ] ]
    return longLen

LONGEST_SUBSEQUENCE_SUCH_THAT_DIFFERENCE_BETWEEN_ADJACENTS_IS_ONE | def longestSubseqWithDiffOne ( arr , n ) :
    dp = [ 1 for i in range ( n ) ]
    for i in range ( n ) :
        for j in range ( i ) :
            if ( ( arr [ i ] == arr [ j ] + 1 ) or ( arr [ i ] == arr [ j ] - 1 ) ) :
                dp [ i ] = max ( dp [ i ] , dp [ j ] + 1 )
    result = 1
    for i in range ( n ) :
        if ( result < dp [ i ] ) :
            result = dp [ i ]
    return result

LOWER_CASE_UPPER_CASE_INTERESTING_FACT | def to_upper(in_list):
    for i in range(len(in_list)):
        if 'a' <= in_list[i] <= 'z':
            in_list[i] = chr(ord(in_list[i]) - ord('a') + ord('A'))
    return ''.join(in_list)

MAKE_LARGEST_PALINDROME_CHANGING_K_DIGITS | def maximumPalinUsingKChanges ( strr , k ) :
    palin = list(strr)
    l = 0
    r = len ( strr ) - 1
    while ( l <= r ) :
        if ( strr [ l ] != strr [ r ] ) :
            palin [ l ] = palin [ r ] = max ( strr [ l ] , strr [ r ] )
            k -= 1
        l += 1
        r -= 1
    if ( k < 0 ) :
        return "Not possible"
    l = 0
    r = len ( strr ) - 1
    while ( l <= r ) :
        if ( l == r ) :
            if ( k > 0 ) :
                palin [ l ] = '9'
        if ( palin [ l ] < '9' ) :
            if ( k >= 2 and palin [ l ] == strr [ l ] and palin [ r ] == strr [ r ] ) :
                k -= 1
                palin [ l ] = palin [ r ] = '9'
            elif ( k >= 1 and ( palin [ l ] != strr [ l ] or palin [ r ] != strr [ r ] ) ) :
                k -= 1
                palin [ l ] = palin [ r ] = '9'
        l += 1
        r -= 1
    return "".join(palin)

MARKOV_MATRIX | def checkMarkov ( m ) :
    for i in range ( 0 , len ( m ) ) :
        sm = 0
        for j in range ( 0 , len ( m [ i ] ) ) :
            sm = sm + m [ i ] [ j ]
        if ( sm != 1 ) :
            return False
    return True

MAXIMIZE_ARRAY_ELEMENTS_UPTO_GIVEN_NUMBER | def findMaxVal ( arr , n , num , maxLimit ) :
    ind = - 1
    val = - 1
    dp = [ [ 0 for i in range ( maxLimit + 1 ) ] for j in range ( n ) ]
    for ind in range ( n ) :
        for val in range ( maxLimit + 1 ) :
            if ( ind == 0 ) :
                if ( num - arr [ ind ] == val or num + arr [ ind ] == val ) :
                    dp [ ind ] [ val ] = 1
                else :
                    dp [ ind ] [ val ] = 0
            else :
                if ( val - arr [ ind ] >= 0 and val + arr [ ind ] <= maxLimit ) :
                    if ( dp [ ind - 1 ] [ val - arr [ ind ] ] == 1 or dp [ ind - 1 ] [ val + arr [ ind ] ] == 1 ) :
                        dp [ ind ] [ val ] = 1
                elif ( val - arr [ ind ] >= 0 ) :
                    dp [ ind ] [ val ] = dp [ ind - 1 ] [ val - arr [ ind ] ]
                elif ( val + arr [ ind ] <= maxLimit ) :
                    dp [ ind ] [ val ] = dp [ ind - 1 ] [ val + arr [ ind ] ]
                else :
                    dp [ ind ] [ val ] = 0
    for val in range ( maxLimit , - 1 , - 1 ) :
        if ( dp [ n - 1 ] [ val ] == 1 ) :
            return val
    return - 1

MAXIMIZE_ARRJ_ARRI_ARRL_ARRK_SUCH_THAT_I_J_K_L | def findMaxValue ( arr , n ) :
    if n < 4 :
        print ( "The array should have atlest 4 elements" )
        return MIN
    table1 , table2 = [ MIN ] * ( n + 1 ) , [ MIN ] * n
    table3 , table4 = [ MIN ] * ( n - 1 ) , [ MIN ] * ( n - 2 )
    for i in range ( n - 1 , - 1 , - 1 ) :
        table1 [ i ] = max ( table1 [ i + 1 ] , arr [ i ] )
    for i in range ( n - 2 , - 1 , - 1 ) :
        table2 [ i ] = max ( table2 [ i + 1 ] , table1 [ i + 1 ] - arr [ i ] )
    for i in range ( n - 3 , - 1 , - 1 ) :
        table3 [ i ] = max ( table3 [ i + 1 ] , table2 [ i + 1 ] + arr [ i ] )
    for i in range ( n - 4 , - 1 , - 1 ) :
        table4 [ i ] = max ( table4 [ i + 1 ] , table3 [ i + 1 ] - arr [ i ] )
    return table4 [ 0 ]

MAXIMIZE_VOLUME_CUBOID_GIVEN_SUM_SIDES_1 | def maxvolume ( s ) :
    length = s // 3 
    s -= length
    breadth = s // 2
    height = s - breadth
    return int ( length * breadth * height )

MAXIMUM_AREA_RECTANGLE_PICKING_FOUR_SIDES_ARRAY | def findArea ( arr , n ) :
    arr.sort ( reverse = True )
    dimension = [ 0 , 0 ]
    i = 0
    j = 0
    while ( i < n - 1 and j < 2 ) :
        if ( arr [ i ] == arr [ i + 1 ] ) :
            dimension [ j ] = arr [ i ]
            j += 1
            i += 1
        i += 1
    return ( dimension [ 0 ] * dimension [ 1 ] )

MAXIMUM_AVERAGE_SUM_PARTITION_ARRAY | def largestSumOfAverages ( A , K ) :
    n = len ( A )
    pre_sum = [ 0 ] * ( n + 1 )
    pre_sum [ 0 ] = 0
    for i in range ( n ) :
        pre_sum [ i + 1 ] = pre_sum [ i ] + A [ i ]
    dp = [ 0 ] * n
    sum = 0
    for i in range ( n ) :
        dp [ i ] = ( pre_sum [ n ] - pre_sum [ i ] ) / ( n - i )
    for k in range ( K - 1 ) :
        for i in range ( n ) :
            for j in range ( i + 1 , n ) :
                dp [ i ] = max ( dp [ i ] , ( pre_sum [ j ] - pre_sum [ i ] ) / ( j - i ) + dp [ j ] )
    return  dp [ 0 ]

MAXIMUM_BINOMIAL_COEFFICIENT_TERM_VALUE | def maxcoefficientvalue ( n ) :
    C = [ [ 0 for x in range ( n + 1 ) ] for y in range ( n + 1 ) ]
    for i in range ( n + 1 ) :
        for j in range ( min ( i , n ) + 1 ) :
            if ( j == 0 or j == i ) :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = ( C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] )
    maxvalue = 0
    for i in range ( n + 1 ) :
        maxvalue = max ( maxvalue , C [ n ] [ i ] )
    return maxvalue

MAXIMUM_CONSECUTIVE_NUMBERS_PRESENT_ARRAY | def findLongestConseqSubseq ( arr , n ) :
    S = set ( )
    for i in range ( n ) :
        S.add ( arr [ i ] )
    ans = 0
    for i in range ( n ) :
        if S.__contains__ ( arr [ i ] ) :
            j = arr [ i ]
            while ( S.__contains__ ( j ) ) :
                j += 1
            ans = max ( ans , j - arr [ i ] )
    return ans

MAXIMUM_CONSECUTIVE_REPEATING_CHARACTER_STRING_1 | def maxRepeating ( str ) :
    n = len ( str )
    count = 0
    res = str [ 0 ]
    cur_count = 1
    for i in range ( n ) :
        if ( i < n - 1 and str [ i ] == str [ i + 1 ] ) :
            cur_count += 1
        else :
            if cur_count > count :
                count = cur_count
                res = str [ i ]
            cur_count = 1
    return res

MAXIMUM_DIFFERENCE_BETWEEN_FREQUENCY_OF_TWO_ELEMENTS_SUCH_THAT_ELEMENT_HAVING_GREATER_FREQUENCY_IS_ALSO_GREATER | def maxdiff ( arr , n ) :
    freq = defaultdict ( lambda : 0 )
    for i in range ( n ) :
        freq [ arr [ i ] ] += 1
    ans = 0
    for i in range ( n ) :
        for j in range ( n ) :
            if freq [ arr [ i ] ] > freq [ arr [ j ] ] and arr [ i ] > arr [ j ] :
                ans = max ( ans , freq [ arr [ i ] ] - freq [ arr [ j ] ] )
            elif freq [ arr [ i ] ] < freq [ arr [ j ] ] and arr [ i ] < arr [ j ] :
                ans = max ( ans , freq [ arr [ j ] ] - freq [ arr [ i ] ] )
    return ans

MAXIMUM_DIFFERENCE_SUM_ELEMENTS_TWO_ROWS_MATRIX | def maxRowDiff ( mat , m , n ) :
    rowSum = [ 0 ] * m
    for i in range ( 0 , m ) :
        sum = 0
        for j in range ( 0 , n ) :
            sum += mat [ i ] [ j ]
        rowSum [ i ] = sum
    max_diff = rowSum [ 1 ] - rowSum [ 0 ]
    min_element = rowSum [ 0 ]
    for i in range ( 1 , m ) :
        if ( rowSum [ i ] - min_element > max_diff ) :
            max_diff = rowSum [ i ] - min_element
        if ( rowSum [ i ] < min_element ) :
            min_element = rowSum [ i ]
    return max_diff

MAXIMUM_DISTANCE_TWO_OCCURRENCES_ELEMENT_ARRAY | def maxDistance ( arr , n ) :
    mp = { }
    maxDict = 0
    for i in range ( n ) :
        if arr [ i ] not in mp.keys ( ) :
            mp [ arr [ i ] ] = i
        else :
            maxDict = max ( maxDict , i - mp [ arr [ i ] ] )
    return maxDict

MAXIMUM_GAMES_PLAYED_WINNER | def maxGameByWinner ( N ) :
    dp = [ 0 for i in range ( N ) ]
    dp [ 0 ] = 1
    dp [ 1 ] = 2
    i = 1
    while dp [ i ] <= N :
        i = i + 1
        dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ]
    return ( i - 1 )

MAXIMUM_LENGTH_PREFIX_ONE_STRING_OCCURS_SUBSEQUENCE_ANOTHER | def maxPrefix ( s , t ) :
    count = 0
    for i in range ( 0 , len ( t ) ) :
        if ( count == len ( s ) ) :
            break
        if ( t [ i ] == s [ count ] ) :
            count = count + 1
    return count

MAXIMUM_LENGTH_SUBSEQUENCE_DIFFERENCE_ADJACENT_ELEMENTS_EITHER_0_1 | def maxLenSub ( arr , n ) :
    mls = [ ]
    max = 0
    for i in range ( n ) :
        mls.append ( 1 )
    for i in range ( n ) :
        for j in range ( i ) :
            if ( abs ( arr [ i ] - arr [ j ] ) <= 1 and mls [ i ] < mls [ j ] + 1 ) :
                mls [ i ] = mls [ j ] + 1
    for i in range ( n ) :
        if ( max < mls [ i ] ) :
            max = mls [ i ]
    return max

MAXIMUM_NUMBER_CHOCOLATES_DISTRIBUTED_EQUALLY_AMONG_K_STUDENTS | def maxNumOfChocolates ( arr , n , k ) :
    um , curr_rem , maxSum = { } , 0 , 0
    sm = [ 0 ] * n
    sm [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        sm [ i ] = sm [ i - 1 ] + arr [ i ]
    for i in range ( n ) :
        curr_rem = sm [ i ] % k
        if ( not curr_rem and maxSum < sm [ i ] ) :
            maxSum = sm [ i ]
        elif ( not curr_rem in um ) :
            um [ curr_rem ] = i
        elif ( maxSum < ( sm [ i ] - sm [ um [ curr_rem ] ] ) ) :
            maxSum = sm [ i ] - sm [ um [ curr_rem ] ]
    return maxSum // k

MAXIMUM_NUMBER_OF_SQUARES_THAT_CAN_BE_FIT_IN_A_RIGHT_ANGLE_ISOSCELES_TRIANGLE | def maxSquare ( b , m ) :
    return ( b // m - 1 ) * ( b // m ) // 2

MAXIMUM_NUMBER_SEGMENTS_LENGTHS_B_C | def maximumSegments ( n , a , b , c ) :
    dp = [ - 1 ] * ( n + 10 )
    dp [ 0 ] = 0
    for i in range ( 0 , n ) :
        if ( dp [ i ] != - 1 ) :
            if ( i + a <= n ) :
                dp [ i + a ] = max ( dp [ i ] + 1 , dp [ i + a ] )
            if ( i + b <= n ) :
                dp [ i + b ] = max ( dp [ i ] + 1 , dp [ i + b ] )
            if ( i + c <= n ) :
                dp [ i + c ] = max ( dp [ i ] + 1 , dp [ i + c ] )
    return dp [ n ]

MAXIMUM_POINTS_INTERSECTION_N_CIRCLES | def intersection ( n ) :
    return n * ( n - 1 )

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY | def maxDiff ( arr , n ) :
    SubsetSum_1 = 0
    SubsetSum_2 = 0
    for i in range ( 0 , n ) :
        isSingleOccurance = True
        for j in range ( i + 1 , n ) :
            if ( arr [ i ] == arr [ j ] ) :
                isSingleOccurance = False
                arr [ i ] = arr [ j ] = 0
                break
        if ( isSingleOccurance == True ) :
            if ( arr [ i ] > 0 ) :
                SubsetSum_1 += arr [ i ]
            else :
                SubsetSum_2 += arr [ i ]
    return abs ( SubsetSum_1 - SubsetSum_2 )

MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY_1 | def maxDiff ( arr , n ) :
    result = 0
    arr.sort ( )
    i = 0
    while i < n-1:
        if ( arr [ i ] !=  arr [ i + 1 ] ) :
            result += abs ( arr [ i ] )
        else:
            i += 1
        i += 1
    if ( arr [ n - 2 ] != arr [ n - 1 ] ) :
        result += abs ( arr [ n - 1 ] )
    return result

MAXIMUM_POSSIBLE_SUM_WINDOW_ARRAY_ELEMENTS_WINDOW_ARRAY_UNIQUE | def returnMaxSum ( A , B , n ) :
    mp = set ( )
    result = 0
    curr_sum = curr_begin = 0
    for i in range ( 0 , n ) :
        while A [ i ] in mp :
            mp.remove ( A [ curr_begin ] )
            curr_sum -= B [ curr_begin ]
            curr_begin += 1
        mp.add ( A [ i ] )
        curr_sum += B [ i ]
        result = max ( result , curr_sum )
    return result

MAXIMUM_PRODUCT_INCREASING_SUBSEQUENCE | def lis ( arr , n ) :
    mpis = [ 0 ] * ( n )
    for i in range ( n ) :
        mpis [ i ] = arr [ i ]
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ i ] > arr [ j ] and mpis [ i ] < ( mpis [ j ] * arr [ i ] ) ) :
                mpis [ i ] = mpis [ j ] * arr [ i ]
    return max ( mpis )

MAXIMUM_PRODUCT_SUBSET_ARRAY | def maxProductSubset ( a , n ) :
    if n == 1 :
        return a [ 0 ]
    max_neg = - 999999999999
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range ( n ) :
        if a [ i ] == 0 :
            count_zero += 1
            continue
        if a [ i ] < 0 :
            count_neg += 1
            max_neg = max ( max_neg , a [ i ] )
        prod = prod + a [ i ]
    if count_zero == n :
        return 0
    if count_neg & 1 :
        if ( count_neg == 1 and count_zero > 0 and count_zero + count_neg == n ) :
            return 0
        prod = int(prod / max_neg)
    return prod

MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_TWICE | def maxProfit ( price , n ) :
    profit = [ 0 ] * n
    max_price = price [ n - 1 ]
    for i in range ( n - 2 , 0 , - 1 ) :
        if price [ i ] > max_price :
            max_price = price [ i ]
        profit [ i ] = max ( profit [ i + 1 ] , max_price - price [ i ] )
    min_price = price [ 0 ]
    for i in range ( 1 , n ) :
        if price [ i ] < min_price :
            min_price = price [ i ]
        profit [ i ] = max ( profit [ i - 1 ] , profit [ i ] + ( price [ i ] - min_price ) )
    result = profit [ n - 1 ]
    return result

MAXIMUM_SUBARRAY_SUM_ARRAY_CREATED_REPEATED_CONCATENATION | def maxSubArraySumRepeated ( a , n , k ) :
    max_so_far = - 2147483648
    max_ending_here = 0
    for i in range ( n * k ) :
        max_ending_here = max_ending_here + a [ i % n ]
        if ( max_so_far < max_ending_here ) :
            max_so_far = max_ending_here
        if ( max_ending_here < 0 ) :
            max_ending_here = 0
    return max_so_far

MAXIMUM_SUBARRAY_SUM_USING_PREFIX_SUM | def maximumSumSubarray ( arr , n ) :
    min_prefix_sum = 0
    res = - math.inf
    prefix_sum = [ ]
    prefix_sum.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        prefix_sum.append ( prefix_sum [ i - 1 ] + arr [ i ] )
    for i in range ( n ) :
        res = max ( res , prefix_sum [ i ] - min_prefix_sum )
        min_prefix_sum = min ( min_prefix_sum , prefix_sum [ i ] )
    return res

MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE | def maxSumWO3Consec ( arr , n ) :
    sum = [ 0 for k in range ( n ) ]
    if n >= 1 :
        sum [ 0 ] = arr [ 0 ]
    if n >= 2 :
        sum [ 1 ] = arr [ 0 ] + arr [ 1 ]
    if n > 2 :
        sum [ 2 ] = max ( sum [ 1 ] , max ( arr [ 1 ] + arr [ 2 ] , arr [ 0 ] + arr [ 2 ] ) )
    for i in range ( 3 , n ) :
        sum [ i ] = max ( max ( sum [ i - 1 ] , sum [ i - 2 ] + arr [ i ] ) , arr [ i ] + arr [ i - 1 ] + sum [ i - 3 ] )
    return sum [ n - 1 ]

MAXIMUM_SUM_2_X_N_GRID_NO_TWO_ELEMENTS_ADJACENT | def maxSum ( grid , n ) :
    incl = max ( grid [ 0 ] [ 0 ] , grid [ 1 ] [ 0 ] )
    excl = 0
    for i in range ( 1 , n ) :
        excl_new = max ( excl , incl )
        incl = excl + max ( grid [ 0 ] [ i ] , grid [ 1 ] [ i ] )
        excl = excl_new
    return max ( excl , incl )

MAXIMUM_SUM_ALTERNATING_SUBSEQUENCE_SUM | def maxAlternateSum ( arr , n ) :
    if ( n == 1 ) :
        return arr [ 0 ]
    dec = [ 0 for i in range ( n + 1 ) ]
    inc = [ 0 for i in range ( n + 1 ) ]
    dec [ 0 ] = inc [ 0 ] = arr [ 0 ]
    flag = 0
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if ( arr [ j ] > arr [ i ] ) :
                dec [ i ] = max ( dec [ i ] , inc [ j ] + arr [ i ] )
                flag = 1
            elif ( arr [ j ] < arr [ i ] and flag == 1 ) :
                inc [ i ] = max ( inc [ i ] , dec [ j ] + arr [ i ] )
    result = - 2147483648
    for i in range ( n ) :
        if ( result < inc [ i ] ) :
            result = inc [ i ]
        if ( result < dec [ i ] ) :
            result = dec [ i ]
    return result

MAXIMUM_SUM_BITONIC_SUBARRAY | def maxSumBitonicSubArr ( arr , n ) :
    msis = [ None ] * n
    msds = [ None ] * n
    max_sum = 0
    msis [ 0 ] = arr [ 0 ]
    for i in range ( 1 , n ) :
        if ( arr [ i ] > arr [ i - 1 ] ) :
            msis [ i ] = msis [ i - 1 ] + arr [ i ]
        else :
            msis [ i ] = arr [ i ]
    msds [ n - 1 ] = arr [ n - 1 ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        if ( arr [ i ] > arr [ i + 1 ] ) :
            msds [ i ] = msds [ i + 1 ] + arr [ i ]
        else :
            msds [ i ] = arr [ i ]
    for i in range ( n ) :
        if ( max_sum < ( msis [ i ] + msds [ i ] - arr [ i ] ) ) :
            max_sum = ( msis [ i ] + msds [ i ] - arr [ i ] )
    return max_sum

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY | def maxSum ( arr , n ) :
    res = - sys.maxsize
    for i in range ( 0 , n ) :
        curr_sum = 0
        for j in range ( 0 , n ) :
            index = int ( ( i + j ) % n )
            curr_sum += j * arr [ index ]
        res = max ( res , curr_sum )
    return res

MAXIMUM_SUM_IARRI_AMONG_ROTATIONS_GIVEN_ARRAY_1 | def maxSum ( arr , n ) :
    cum_sum = 0
    for i in range ( 0 , n ) :
        cum_sum += arr [ i ]
    curr_val = 0
    for i in range ( 0 , n ) :
        curr_val += i * arr [ i ]
    res = curr_val
    for i in range ( 1 , n ) :
        next_val = ( curr_val - ( cum_sum - arr [ i - 1 ] ) + arr [ i - 1 ] * ( n - 1 ) )
        curr_val = next_val
        res = max ( res , next_val )
    return res

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE | def maxSumPairWithDifferenceLessThanK ( arr , N , K ) :
    arr.sort ( )
    dp = [ 0 ] * N
    dp [ 0 ] = 0
    for i in range ( 1 , N ) :
        dp [ i ] = dp [ i - 1 ]
        if ( arr [ i ] - arr [ i - 1 ] < K ) :
            if ( i >= 2 ) :
                dp [ i ] = max ( dp [ i ] , dp [ i - 2 ] + arr [ i ] + arr [ i - 1 ] )
            else :
                dp [ i ] = max ( dp [ i ] , arr [ i ] + arr [ i - 1 ] )
    return dp [ N - 1 ]

MAXIMUM_SUM_PAIRS_SPECIFIC_DIFFERENCE_1 | def maxSumPairWithDifferenceLessThanK ( arr , N , k ) :
    maxSum = 0
    arr.sort ( )
    i = N - 1
    while ( i > 0 ) :
        if ( arr [ i ] - arr [ i - 1 ] < k ) :
            maxSum += arr [ i ]
            maxSum += arr [ i - 1 ]
            i -= 1
        i -= 1
    return maxSum

MAXIMUM_SUM_SUBARRAY_REMOVING_ONE_ELEMENT | def maxSumSubarrayRemovingOneEle ( arr , n ) :
    fw = [ 0 for k in range ( n ) ]
    bw = [ 0 for k in range ( n ) ]
    cur_max , max_so_far = arr [ 0 ] , arr [ 0 ]
    for i in range (1, n ) :
        cur_max = max ( arr [ i ] , cur_max + arr [ i ] )
        max_so_far = max ( max_so_far , cur_max )
        fw [ i ] = cur_max
    cur_max = max_so_far = bw [ n - 1 ] = arr [ n - 1 ]
    i = n - 2
    while i >= 0 :
        cur_max = max ( arr [ i ] , cur_max + arr [ i ] )
        max_so_far = max ( max_so_far , cur_max )
        bw [ i ] = cur_max
        i -= 1
    fans = max_so_far
    for i in range ( 1 , n - 1 ) :
        fans = max ( fans , fw [ i - 1 ] + bw [ i + 1 ] )
    return fans

MAXIMUM_SUM_SUBSEQUENCE_LEAST_K_DISTANT_ELEMENTS | def maxSum ( arr , N , k ) :
    MS = [ 0 for i in range ( N ) ]
    MS [ N - 1 ] = arr [ N - 1 ]
    for i in range ( N - 2 , - 1 , - 1 ) :
        if ( i + k + 1 >= N ) :
            MS [ i ] = max ( arr [ i ] , MS [ i + 1 ] )
        else :
            MS [ i ] = max ( arr [ i ] + MS [ i + k + 1 ] , MS [ i + 1 ] )
    return MS [ 0 ]

MAXIMUM_TRIPLET_SUM_ARRAY | def maxTripletSum ( arr , n ) :
    sm = - 1000000
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            for k in range ( j + 1 , n ) :
                if ( sm < ( arr [ i ] + arr [ j ] + arr [ k ] ) ) :
                    sm = arr [ i ] + arr [ j ] + arr [ k ]
    return sm

MAXIMUM_TRIPLET_SUM_ARRAY_1 | def maxTripletSum ( arr , n ) :
    arr.sort ( )
    return ( arr [ n - 1 ] + arr [ n - 2 ] + arr [ n - 3 ] )

MAXIMUM_VALUE_CHOICE_EITHER_DIVIDING_CONSIDERING | def maxDP ( n ) :
    res = list ( )
    res.append ( 0 )
    res.append ( 1 )
    i = 2
    while i < n + 1 :
        res.append ( max ( i , ( res [ int ( i / 2 ) ] + res [ int ( i / 3 ) ] + res [ int ( i / 4 ) ] + res [ int ( i / 5 ) ] ) ) )
        i = i + 1
    return res [ n ]

MAXIMUM_WEIGHT_PATH_ENDING_ELEMENT_LAST_ROW_MATRIX | def maxCost ( mat , N ) :
    dp = [ [ 0 for i in range ( N ) ] for j in range ( N ) ]
    dp [ 0 ] [ 0 ] = mat [ 0 ] [ 0 ]
    for i in range ( 1 , N ) :
        dp [ i ] [ 0 ] = mat [ i ] [ 0 ] + dp [ i - 1 ] [ 0 ]
    for i in range ( 1 , N ) :
        for j in range ( 1 , min ( i + 1 , N ) ) :
            dp [ i ] [ j ] = mat [ i ] [ j ] + \
                max ( dp [ i - 1 ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    result = 0
    for i in range ( N ) :
        if ( result < dp [ N - 1 ] [ i ] ) :
            result = dp [ N - 1 ] [ i ]
    return result

MEDIAN_OF_TWO_SORTED_ARRAYS | def getMedian ( ar1 , ar2 , n ) :
    i = 0
    j = 0
    m1 = - 1
    m2 = - 1
    count = 0
    while count < n + 1 :
        count += 1
        if i == n :
            m1 = m2
            m2 = ar2 [ 0 ]
            break
        elif j == n :
            m1 = m2
            m2 = ar1 [ 0 ]
            break
        if ar1 [ i ] < ar2 [ j ] :
            m1 = m2
            m2 = ar1 [ i ]
            i += 1
        else :
            m1 = m2
            m2 = ar2 [ j ]
            j += 1
    return int(( m1 + m2 ) / 2)

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS | def middleOfThree ( a , b , c ) :
    if ( ( a < b and b < c ) or ( c < b and b < a ) ) :
        return b
    if ( ( b < a and a < c ) or ( c < a and a < b ) ) :
        return a
    else :
        return c

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_1 | def middleOfThree ( a , b , c ) :
    if a > b :
        if ( b > c ) :
            return b
        elif ( a > c ) :
            return c
        else :
            return a
    else :
        if ( a > c ) :
            return a
        elif ( b > c ) :
            return c
        else :
            return b

MIDDLE_OF_THREE_USING_MINIMUM_COMPARISONS_2 | def middleOfThree ( a , b , c ) :
    x = a - b
    y = b - c
    z = a - c
    if x * y > 0 :
        return b
    elif ( x * z > 0 ) :
        return c
    else :
        return a

MINIMIZE_SUM_PRODUCT_TWO_ARRAYS_PERMUTATIONS_ALLOWED | def minValue ( A , B , n ) :
    sorted ( A )
    sorted ( B )
    result = 0
    for i in range ( n ) :
        result += ( A [ i ] * B [ n - i - 1 ] )
    return result

MINIMIZE_THE_MAXIMUM_DIFFERENCE_BETWEEN_THE_HEIGHTS | def getMinDiff ( arr , n , k ) :
    if ( n == 1 ) :
        return 0
    arr.sort ( )
    ans = arr [ n - 1 ] - arr [ 0 ]
    small = arr [ 0 ] + k
    big = arr [ n - 1 ] - k
    if ( small > big ) :
        small , big = big , small
    for i in range ( 1 , n - 1 ) :
        subtract = arr [ i ] - k
        add = arr [ i ] + k
        if ( subtract >= small or add <= big ) :
            continue
        if ( big - subtract <= add - small ) :
            small = subtract
        else :
            big = add
    return min ( ans , big - small )

MINIMIZE_THE_SUM_OF_DIGITS_OF_A_AND_B_SUCH_THAT_A_B_N | def minSum ( n ) :
    sum = 0
    while ( n > 0 ) :
        sum += ( n % 10 )
        n //= 10
    if ( sum == 1 ) :
        return 10
    return sum

MINIMUM_COST_CONNECT_WEIGHTED_NODES_REPRESENTED_ARRAY | def minimum_cost ( a , n ) :
    mn = sys.maxsize
    sum = 0
    for i in range ( n ) :
        mn = min ( a [ i ] , mn )
        sum += a [ i ]
    return mn * ( sum - mn )

MINIMUM_COST_MAKE_ARRAY_SIZE_1_REMOVING_LARGER_PAIRS | def cost ( a , n ) :
    return ( ( n - 1 ) * min ( a ) )

MINIMUM_COST_MAKE_LONGEST_COMMON_SUBSEQUENCE_LENGTH_K | def solve ( X , Y , l , r , k , dp ) :
    if k == 0 :
        return 0
    if l < 0 or r < 0 :
        return 1000000000
    if dp [ l ] [ r ] [ k ] != - 1 :
        return dp [ l ] [ r ] [ k ]
    cost = ( ( ord ( X [ l ] ) - ord ( 'a' ) ) ^ ( ord ( Y [ r ] ) - ord ( 'a' ) ) )
    dp [ l ] [ r ] [ k ] = min ( [ cost + solve ( X , Y , l - 1 , r - 1 , k - 1 , dp ) , solve ( X , Y , l - 1 , r , k , dp ) , solve ( X , Y , l , r - 1 , k , dp ) ] )
    return dp [ l ] [ r ] [ k ]

MINIMUM_COST_SORT_MATRIX_NUMBERS_0_N2_1 | def calculateEnergy ( mat , n ) :
    tot_energy = 0
    for i in range ( n ) :
        for j in range ( n ) :
            q = mat [ i ] [ j ] // n
            i_des = q
            j_des = mat [ i ] [ j ] - ( n * q )
            tot_energy += ( abs ( i_des - i ) + abs ( j_des - j ) )
    return tot_energy

MINIMUM_COST_TO_FILL_GIVEN_WEIGHT_IN_A_BAG | def MinimumCost ( cost , n , W ) :
    val = list ( )
    wt = list ( )
    size = 0
    for i in range ( n ) :
        if ( cost [ i ] != - 1 ) :
            val.append ( cost [ i ] )
            wt.append ( i + 1 )
            size += 1
    n = size
    min_cost = [ [ 0 for i in range ( W + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( W + 1 ) :
        min_cost [ 0 ] [ i ] = INF
    for i in range ( 1 , n + 1 ) :
        min_cost [ i ] [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , W + 1 ) :
            if ( wt [ i - 1 ] > j ) :
                min_cost [ i ] [ j ] = min_cost [ i - 1 ] [ j ]
            else :
                min_cost [ i ] [ j ] = min ( min_cost [ i - 1 ] [ j ] , min_cost [ i ] [ j - wt [ i - 1 ] ] + val [ i - 1 ] )
    if ( min_cost [ n ] [ W ] == INF ) :
        return - 1
    else :
        return min_cost [ n ] [ W ]

MINIMUM_FLIP_REQUIRED_MAKE_BINARY_MATRIX_SYMMETRIC_1 | def minimumflip ( mat , n ) :
    flip = 0
    for i in range ( n ) :
        for j in range ( i ) :
            if mat [ i ] [ j ] != mat [ j ] [ i ] :
                flip += 1
    return flip

MINIMUM_INCREMENT_K_OPERATIONS_MAKE_ELEMENTS_EQUAL | def minOps ( arr , n , k ) :
    max1 = max ( arr )
    res = 0
    for i in range ( 0 , n ) :
        if ( ( max1 - arr [ i ] ) % k != 0 ) :
            return - 1
        else :
            res += ( max1 - arr [ i ] ) / k
    return int ( res )

MINIMUM_INSERTIONS_SORT_ARRAY | def minInsertionStepToSortArray ( arr , N ) :
    lis = [ 0 ] * N
    for i in range ( N ) :
        lis [ i ] = 1
    for i in range ( 1 , N ) :
        for j in range ( i ) :
            if ( arr [ i ] >= arr [ j ] and lis [ i ] < lis [ j ] + 1 ) :
                lis [ i ] = lis [ j ] + 1
    max = 0
    for i in range ( N ) :
        if ( max < lis [ i ] ) :
            max = lis [ i ]
    return ( N - max )

MINIMUM_LENGTH_SUBARRAY_SUM_GREATER_GIVEN_VALUE_1 | def smallestSubWithSum ( arr , n , x ) :
    curr_sum = 0
    min_len = n + 1
    start = 0
    end = 0
    while ( end < n ) :
        while ( curr_sum <= x and end < n ) :
            if ( curr_sum <= 0 and x > 0 ) :
                start = end
                curr_sum = 0
            curr_sum += arr [ end ]
            end += 1
        while ( curr_sum > x and start < n ) :
            if ( end - start < min_len ) :
                min_len = end - start
            curr_sum -= arr [ start ]
            start += 1
    return min_len

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_1 | def minJumps ( arr , n ) :
    jumps = [ 0 for i in range ( n ) ]
    if ( n == 0 ) or ( arr [ 0 ] == 0 ) :
        return float ( 'inf' )
    jumps [ 0 ] = 0
    for i in range ( 1 , n ) :
        jumps [ i ] = float ( 'inf' )
        for j in range ( i ) :
            if ( i <= j + arr [ j ] ) and ( jumps [ j ] != float ( 'inf' ) ) :
                jumps [ i ] = min ( jumps [ i ] , jumps [ j ] + 1 )
                break
    return jumps [ n - 1 ]

MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_2 | def minJumps ( arr , n ) :
    jumps = [ 0 for i in range ( n ) ]
    for i in range ( n - 2 , - 1 , - 1 ) :
        if ( arr [ i ] == 0 ) :
            jumps [ i ] = float ( 'inf' )
        elif ( arr [ i ] >= n - i - 1 ) :
            jumps [ i ] = 1
        else :
            min = float ( 'inf' )
            for j in range ( i + 1 , n ) :
                if ( j <= arr [ i ] + i ) :
                    if ( min > jumps [ j ] ) :
                        min = jumps [ j ]
            if ( min != float ( 'inf' ) ) :
                jumps [ i ] = min + 1
            else :
                jumps [ i ] = min
    return jumps [ 0 ]

MINIMUM_NUMBER_OF_SQUARES_WHOSE_SUM_EQUALS_TO_GIVEN_NUMBER_N_1 | def getMinSquares ( n ) :
    dp = [ 0 , 1 , 2 , 3 ]
    for i in range ( 4 , n + 1 ) :
        dp.append ( i )
        for x in range ( 1 , int ( ceil ( sqrt ( i ) ) ) + 1 ) :
            temp = x * x ;
            if temp > i :
                break
            else :
                dp [ i ] = min ( dp [ i ] , 1 + dp [ i - temp ] )
    return dp [ n ]

MINIMUM_NUMBER_SUBSETS_DISTINCT_ELEMENTS | def subset ( ar , n ) :
    res = 0
    ar.sort ( )
    i = 0
    while i < n:
        count = 1
        j = i
        while j < n - 1:
            if ar [ j ] == ar [ j + 1 ] :
                count += 1
            else :
                break
            j += 1
        i = j
        i += 1
        res = max ( res , count )
    return res

MINIMUM_NUMBER_SUBSETS_DISTINCT_ELEMENTS_1 | def subset ( arr , n ) :
    maxv = max(arr)
    minv = min(arr)
    mp = { i : 0 for i in range ( minv, maxv+1 ) }
    for i in range ( n ) :
        mp [ arr [ i ] ] += 1
    res = 0
    for key , value in mp.items ( ) :
        res = max ( res , value )
    return res

MINIMUM_OPERATION_MAKE_ELEMENTS_EQUAL_ARRAY | def minOperation ( arr , n ) :
    Hash = defaultdict ( lambda : 0 )
    for i in range ( 0 , n ) :
        Hash [ arr [ i ] ] += 1
    max_count = 0
    for i in Hash :
        if max_count < Hash [ i ] :
            max_count = Hash [ i ]
    return n - max_count

MINIMUM_PERIMETER_N_BLOCKS | def minPerimeter ( n ) :
    l = int ( math.sqrt ( n ) )
    sq = l * l
    if ( sq == n ) :
        return l * 4
    else :
        row = int ( n / l )
        perimeter = 2 * ( l + row )
        if ( n % l != 0 ) :
            perimeter += 2
        return perimeter

MINIMUM_PRODUCT_K_INTEGERS_ARRAY_POSITIVE_INTEGERS | def minProduct(arr, n, k):
    pq = []
    for i in range(n):
        heapq.heappush(pq, arr[i])
    count = 0
    ans = 1
    while pq and count < k:
        ans += heapq.heappop(pq)
        count += 1
    return ans

MINIMUM_PRODUCT_SUBSET_ARRAY | def minProductSubset ( a , n ) :
    if ( n == 1 ) :
        return a [ 0 ]
    max_neg = float ( '-inf' )
    min_pos = float ( 'inf' )
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range ( 0 , n ) :
        if ( a [ i ] == 0 ) :
            count_zero = count_zero + 1
            continue
        if ( a [ i ] < 0 ) :
            count_neg = count_neg + 1
            max_neg = max ( max_neg , a [ i ] )
        if ( a [ i ] > 0 ) :
            min_pos = min ( min_pos , a [ i ] )
        prod = prod * a [ i ]
    if ( count_zero == n or ( count_neg == 0 and count_zero > 0 ) ) :
        return 0
    if ( count_neg == 0 ) :
        return min_pos
    if ( ( count_neg & 1 ) == 0 and count_neg != 0 ) :
        prod = int ( prod / max_neg )
    return prod

MINIMUM_ROOMS_FOR_M_EVENTS_OF_N_BATCHES_WITH_GIVEN_SCHEDULE | def findMinRooms ( slots , n , m ) :
    counts = [ 0 ] * m
    for i in range ( n ) :
        for j in range ( m ) :
            if i < len(slots) and j < len(slots[i]):
                if ( slots [ i ] [ j ] == '1' ) :
                    counts [ j ] += 1
    return max ( counts )

MINIMUM_ROTATIONS_REQUIRED_GET_STRING | def findRotations ( str ) :
    tmp = str + str
    n = len ( str )
    for i in range ( 1 , n + 1 ) :
        substring = tmp [ i : n ]
        if ( str == substring ) :
            return i
    return n

MINIMUM_ROTATIONS_UNLOCK_CIRCULAR_LOCK | def minRotation ( input , unlock_code ) :
    rotation = 0
    while ( input > 0 or unlock_code > 0 ) :
        input_digit = input % 10
        code_digit = unlock_code % 10
        rotation += min ( abs ( input_digit - code_digit ) , 10 - abs ( input_digit - code_digit ) )
        input = int ( input / 10 )
        unlock_code = int ( unlock_code / 10 )
    return rotation

MINIMUM_STEPS_MINIMIZE_N_PER_GIVEN_CONDITION | def getMinSteps ( n ) :
    table = [ 0 ] * ( n + 1 )
    for i in range ( n + 1 ) :
        table [ i ] = n - i
    for i in range ( n , 0 , - 1 ) :
        if ( not ( i % 2 ) ) :
            table [ i // 2 ] = min ( table [ i ] + 1 , table [ i // 2 ] )
        if ( not ( i % 3 ) ) :
            table [ i // 3 ] = min ( table [ i ] + 1 , table [ i // 3 ] )
    return table [ 1 ]

MINIMUM_SUM_CHOOSING_MINIMUM_PAIRS_ARRAY | def minSum ( A, n ) :
    min_val = min ( A ) ;
    return min_val * ( n - 1 )

MINIMUM_SUM_PRODUCT_TWO_ARRAYS | def minproduct ( a , b , n , k ) :
    diff = 0
    res = 0
    temp = 0
    for i in range ( n ) :
        pro = a [ i ] * b [ i ]
        res = res + pro
        if ( pro < 0 and b [ i ] < 0 ) :
            temp = ( a [ i ] + 2 * k ) * b [ i ]
        elif ( pro < 0 and a [ i ] < 0 ) :
            temp = ( a [ i ] - 2 * k ) * b [ i ]
        elif ( pro > 0 and a [ i ] < 0 ) :
            temp = ( a [ i ] + 2 * k ) * b [ i ]
        elif ( pro > 0 and a [ i ] > 0 ) :
            temp = ( a [ i ] - 2 * k ) * b [ i ]
        d = abs ( pro - temp )
        if ( d > diff ) :
            diff = d
    return res - diff

MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED | def minSum ( arr , n ) :
    dp = [ 0 ] * n
    if ( n == 1 ) :
        return arr [ 0 ]
    if ( n == 2 ) :
        return min ( arr [ 0 ] , arr [ 1 ] )
    if ( n == 3 ) :
        return min ( arr [ 0 ] , min ( arr [ 1 ] , arr [ 2 ] ) )
    if ( n == 4 ) :
        return min ( min ( arr [ 0 ] , arr [ 1 ] ) , min ( arr [ 2 ] , arr [ 3 ] ) )
    dp [ 0 ] = arr [ 0 ]
    dp [ 1 ] = arr [ 1 ]
    dp [ 2 ] = arr [ 2 ]
    dp [ 3 ] = arr [ 3 ]
    for i in range ( 4 , n ) :
        dp [ i ] = arr [ i ] + min ( min ( dp [ i - 1 ] , dp [ i - 2 ] ) , min ( dp [ i - 3 ] , dp [ i - 4 ] ) )
    return min ( min ( dp [ n - 1 ] , dp [ n - 2 ] ) , min ( dp [ n - 4 ] , dp [ n - 3 ] ) )

MINIMUM_SUM_TWO_NUMBERS_FORMED_DIGITS_ARRAY | def solve ( arr , n ) :
    arr.sort ( )
    a = 0
    b = 0
    for i in range ( n ) :
        if ( i % 2 != 0 ) :
            a = a * 10 + arr [ i ]
        else :
            b = b * 10 + arr [ i ]
    return a + b

MINIMUM_TIME_WRITE_CHARACTERS_USING_INSERT_DELETE_COPY_OPERATION | def minTimeForWritingChars ( N , insrt , remov , cpy ) :
    if N == 0 :
        return 0
    if N == 1 :
        return insrt
    dp = [ 0 ] * ( N + 1 )
    for i in range ( 1 , N + 1 ) :
        if i % 2 == 0 :
            dp [ i ] = min ( dp [ i - 1 ] + insrt , dp [ i // 2 ] + cpy )
        else :
            dp [ i ] = min ( dp [ i - 1 ] + insrt , dp [ ( i + 1 ) // 2 ] + cpy + remov )
    return dp [ N ]

MINIMUM_XOR_VALUE_PAIR | def minXOR ( arr , n ) :
    min_xor = 999999
    val = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            val = arr [ i ] ^ arr [ j ]
            min_xor = min ( min_xor , val )
    return min_xor

MINIMUM_XOR_VALUE_PAIR_1 | def minXOR ( arr , n ) :
    arr = arr [ : n ]
    arr.sort ( )
    minXor = int ( sys.float_info.max )
    val = 0
    for i in range ( 0 , n - 1 ) :
        val = arr [ i ] ^ arr [ i + 1 ]
        minXor = min ( minXor , val )
    return minXor

MIRROR_CHARACTERS_STRING | def compute ( str , n ) :
    reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba"
    l = len ( str )
    answer = ""
    for i in range ( 0 , n ) :
        if i < l:
            answer = answer + str [ i ]
    for i in range ( n , l ) :
        answer = ( answer + reverseAlphabet [ ord ( str [ i ] ) - ord ( "a" ) ] )
    return answer

MODULAR_EXPONENTIATION_POWER_IN_MODULAR_ARITHMETIC | def power ( x , y , p ) :
    res = 1
    x = x % p
    while ( y > 0 ) :
        if ( ( y & 1 ) == 1 ) :
            res = ( res * x ) % p
        y = y >> 1
        x = ( x * x ) % p
    return res

MODULUS_TWO_FLOAT_DOUBLE_NUMBERS | def findMod ( a , b ) :
    if ( a < 0 ) :
        a = - a
    if ( b < 0 ) :
        b = - b
    mod = a
    while ( mod >= b ) :
        mod = mod - b
    if ( a < 0 ) :
        return - mod
    return mod

MOVE_VE_ELEMENTS_END_ORDER_EXTRA_SPACE_ALLOWED | def segregateElements ( arr , n ) :
    temp = [ 0 for k in range ( n ) ]
    j = 0
    for i in range ( n ) :
        if ( arr [ i ] >= 0 ) :
            temp [ j ] = arr [ i ]
            j += 1
    if ( j == n or j == 0 ) :
        return
    for i in range ( n ) :
        if ( arr [ i ] < 0 ) :
            temp [ j ] = arr [ i ]
            j += 1
    for k in range ( n ) :
        arr [ k ] = temp [ k ]

MULTIPLY_AN_INTEGER_WITH_3_5 | def multiplyWith3Point5 ( x ) :
    return ( x << 1 ) + x + ( x >> 1 )

MULTIPLY_LARGE_INTEGERS_UNDER_LARGE_MODULO | def moduloMultiplication ( a , b , mod ) :
    res = 0 ;
    a = a % mod ;
    while ( b ) :
        if ( b & 1 ) :
            res = ( res + a ) % mod ;
        a = ( 2 * a ) % mod ;
        b >>= 1 ;
    return res ;

MULTIPLY_TWO_NUMBERS_WITHOUT_USING_MULTIPLY_DIVISION_BITWISE_OPERATORS_AND_NO_LOOPS | def multiply ( x , y ) :
    if ( y == 0 ) :
        return 0
    if ( y > 0 ) :
        return ( x + multiply ( x , y - 1 ) )
    if ( y < 0 ) :
        return - multiply ( x , - y )

NEWMAN_CONWAY_SEQUENCE_1 | def sequence ( n ) :
    f = array.array ( 'i' , [ 0 , 1 , 1 ] )
    for i in range ( 3 , n + 1 ) :
        r = f [ f [ i - 1 ] ] + f [ i - f [ i - 1 ] ]
        f.append ( r )
    return f[n]

NEXT_HIGHER_NUMBER_WITH_SAME_NUMBER_OF_SET_BITS | def snoob ( x ) :
    next = 0
    if ( x ) :
        rightOne = x & - ( x )
        nextHigherOneBit = x + int ( rightOne )
        rightOnesPattern = x ^ int ( nextHigherOneBit )
        rightOnesPattern = ( int ( rightOnesPattern ) / int ( rightOne ) )
        rightOnesPattern = int ( rightOnesPattern ) >> 2
        next = nextHigherOneBit | rightOnesPattern
    return next

NEXT_POWER_OF_2 | def nextPowerOf2 ( n ) :
    count = 0
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( n != 0 ) :
        n >>= 1
        count += 1
    return 1 << count

NEXT_POWER_OF_2_1 | def nextPowerOf2 ( n ) :
    p = 1
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( p < n ) :
        p <<= 1
    return p

NEXT_POWER_OF_2_2 | def nextPowerOf2 ( n ) :
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n

NON_REPEATING_ELEMENT | def firstNonRepeating ( arr , n ) :
    for i in range ( n ) :
        j = 0
        while ( j < n ) :
            if ( i != j and arr [ i ] == arr [ j ] ) :
                break
            j += 1
        if ( j == n ) :
            return arr [ i ]
    return - 1

NON_REPEATING_ELEMENT_1 | def firstNonRepeating ( arr , n ) :
    mp = defaultdict ( lambda : 0 )
    for i in range ( n ) :
        mp [ arr [ i ] ] += 1
    for i in range ( n ) :
        if mp [ arr [ i ] ] == 1 :
            return arr [ i ]
    return - 1

NTH_EVEN_LENGTH_PALINDROME | def evenlength ( n ) :
    res = n
    for j in range ( len ( n ) - 1 , - 1 , - 1 ) :
        res += n [ j ]
    return res

NTH_MULTIPLE_NUMBER_FIBONACCI_SERIES | def findPosition ( k , n ) :
    f1 = 0
    f2 = 1
    i = 2
    while i != 0 :
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        if f2 % k == 0 :
            return n * i
        i += 1
    return

NTH_NON_FIBONACCI_NUMBER | def nonFibonacci ( n ) :
    prevPrev = 1
    prev = 2
    curr = 3
    while n > 0 :
        prevPrev = prev
        prev = curr
        curr = prevPrev + prev
        n = n - ( curr - prev - 1 )
    n = n + ( curr - prev - 1 )
    return prev + n

NTH_PENTAGONAL_NUMBER | def pentagonalNum ( n ) :
    return ( 3 * n * n - n ) / 2

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS | def countDigits ( a , b ) :
    count = 0
    p = abs ( a * b )
    if ( p == 0 ) :
        return 1
    while ( p > 0 ) :
        count = count + 1
        p = p // 10
    return count

NUMBER_DIGITS_PRODUCT_TWO_NUMBERS_1 | def countDigits ( a , b ) :
    if ( a == 0 or b == 0 ) :
        return 1
    return math.floor ( math.log10 ( abs ( a ) ) + math.log10 ( abs ( b ) ) ) + 1

NUMBER_DIGITS_REMOVED_MAKE_NUMBER_DIVISIBLE_3 | def divisible ( num ) :
    n = len ( num )
    sum = 0
    for i in range ( n ) :
        sum += ord ( num [ i ] )
    if ( sum % 3 == 0 ) :
        return 0
    if ( n == 1 ) :
        return - 1
    for i in range ( n ) :
        if ( sum % 3 == ord ( num [ i ] ) % 3 ) :
            return 1
    if ( n == 2 ) :
        return - 1
    return 2

NUMBER_INDEXES_EQUAL_ELEMENTS_GIVEN_RANGE | def answer_query ( a , n , l , r ) :
    count = 0
    for i in range ( l , r ) :
        if ( a [ i ] == a [ i + 1 ] ) :
            count += 1
    return count

NUMBER_IS_DIVISIBLE_BY_29_OR_NOT | def isDivisible ( n ) :
    while ( int ( n / 100 ) ) :
        last_digit = int ( n % 10 )
        n = int ( n / 10 )
        n += last_digit * 3
    return ( n % 29 == 0 )

NUMBER_NON_NEGATIVE_INTEGRAL_SOLUTIONS_B_C_N | def countIntegralSolutions ( n ) :
    result = 0
    for i in range ( n + 1 ) :
        for j in range ( n + 1 ) :
            for k in range ( n + 1 ) :
                if i + j + k == n :
                    result += 1
    return result

NUMBER_N_DIGITS_NON_DECREASING_INTEGERS | def nonDecNums ( n ) :
    a = np.zeros ( ( n + 1 , 10 ) )
    for i in range ( 10 ) :
        a [ 0 ] [ i ] = 1
    for i in range ( 1 , n + 1 ) :
        a [ i ] [ 9 ] = 1
    for i in range ( 1 , n + 1 ) :
        for j in range ( 8 , - 1 , - 1 ) :
            a [ i ] [ j ] = a [ i - 1 ] [ j ] + a [ i ] [ j + 1 ]
    return int ( a [ n ] [ 0 ] )

NUMBER_N_DIGIT_STEPPING_NUMBERS | def answer ( n ) :
    dp = [ [ 0 for x in range ( 10 ) ] for y in range ( n + 1 ) ]
    if ( n == 1 ) :
        return 10
    for j in range ( 10 ) :
        dp [ 1 ] [ j ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 10 ) :
            if ( j == 0 ) :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ]
            elif ( j == 9 ) :
                dp [ i ] [ j ] = dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] )
    sum = 0
    for j in range ( 1 , 10 ) :
        sum = sum + dp [ n ] [ j ]
    return sum

NUMBER_OF_PAIRS_IN_AN_ARRAY_HAVING_SUM_EQUAL_TO_PRODUCT | def sumEqualProduct ( a , n ) :
    zero = 0
    two = 0
    for i in range ( n ) :
        if a [ i ] == 0 :
            zero += 1
        if a [ i ] == 2 :
            two += 1
    cnt = ( zero * ( zero - 1 ) ) // 2 + \
        ( two * ( two - 1 ) ) // 2
    return cnt

NUMBER_RECTANGLES_NM_GRID | def rectCount ( n , m ) :
    return ( m * n * ( n + 1 ) * ( m + 1 ) ) // 4

NUMBER_SUBSEQUENCES_AB_STRING_REPEATED_K_TIMES | def countOccurrences ( s , K ) :
    n = len ( s )
    c1 = 0
    c2 = 0
    C = 0
    for i in range ( n ) :
        if s [ i ] == 'a' :
            c1 += 1
        if s [ i ] == 'b' :
            c2 += 1
            C += c1
    return C * K + int ( K * ( K - 1 ) / 2 ) * c1 * c2

NUMBER_SUBSEQUENCES_STRING_DIVISIBLE_N | def countDivisibleSubseq ( str , n ) :
    l = len ( str )
    dp = [ [ 0 for x in range ( n ) ] for y in range ( l ) ]
    dp [ 0 ] [ ( ord ( str [ 0 ] ) - ord ( '0' ) ) % n ] += 1
    for i in range ( 1 , l ) :
        dp [ i ] [ ( ord ( str [ i ] ) - ord ( '0' ) ) % n ] += 1
        for j in range ( n ) :
            dp [ i ] [ j ] += dp [ i - 1 ] [ j ]
            dp [ i ] [ ( j * 10 + ( ord ( str [ i ] ) - ord ( '0' ) ) ) % n ] += dp [ i - 1 ] [ j ]
    return dp [ l - 1 ] [ 0 ]

NUMBER_SUBSTRINGS_STRING | def countNonEmptySubstr ( str ) :
    n = len ( str )
    return int ( n * ( n + 1 ) / 2 )

NUMBER_UNIQUE_RECTANGLES_FORMED_USING_N_UNIT_SQUARES | def countRect ( n ) :
    ans = 0
    for length in range ( 1 , int ( math.sqrt ( n ) ) + 1 ) :
        height = length
        while ( height * length <= n ) :
            ans += 1
            height += 1
    return ans

NUMBER_VISIBLE_BOXES_PUTTING_ONE_INSIDE_ANOTHER | def minimumBox ( arr , n ) :
    q = collections.deque ( [ ] )
    arr = arr [ : n ]
    arr.sort ( )
    q.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        now = q [ 0 ]
        if ( arr [ i ] >= 2 * now ) :
            q.popleft ( )
        q.append ( arr [ i ] )
    return len ( q )

NUMBER_WHICH_HAS_THE_MAXIMUM_NUMBER_OF_DISTINCT_PRIME_FACTORS_IN_RANGE_M_TO_N | def maximumNumberDistinctPrimeRange ( m , n ) :
    factorCount = [ 0 ] * ( n + 1 )
    prime = [ False ] * ( n + 1 )
    for i in range ( n + 1 ) :
        factorCount [ i ] = 0
        prime [ i ] = True
    for i in range ( 2 , n + 1 ) :
        if ( prime [ i ] == True ) :
            factorCount [ i ] = 1
            for j in range ( i * 2 , n + 1 , i ) :
                factorCount [ j ] += 1
                prime [ j ] = False
    max = factorCount [ m ]
    num = m
    for i in range ( m , n + 1 ) :
        if ( factorCount [ i ] > max ) :
            max = factorCount [ i ]
            num = i
    return num

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN | def findNth ( n ) :
    count = 0
    for curr in itertools.count ( ) :
        sum = 0
        x = curr
        while ( x ) :
            sum = sum + x % 10
            x = x // 10
        if ( sum == 10 ) :
            count = count + 1
        if ( count == n ) :
            return curr
    return - 1

N_TH_NUMBER_WHOSE_SUM_OF_DIGITS_IS_TEN_2 | def findNth ( n ) :
    nthElement = 19 + ( n - 1 ) * 9
    outliersCount = int ( math.log10 ( nthElement ) ) - 1
    nthElement += 9 * outliersCount
    return nthElement

N_TH_ROOT_NUMBER | def nthRoot ( A , N ) :
    random.seed ( 1 )
    xPre = random.uniform ( 1 , 101 ) % 10
    eps = 0.001
    delX = 2147483647
    xK = 0.0
    while ( delX > eps ) :
        xK = ( ( N - 1.0 ) * xPre + A / pow ( xPre , N - 1 ) ) / N
        delX = abs ( xK - xPre )
        xPre = xK
    return xK

N_TH_TERM_SERIES_2_12_36_80_150 | def nthTerm ( n ) :
    return ( n * n ) + ( n * n * n )

OVERLAPPING_SUM_TWO_ARRAY | def findSum ( A , B , n ) :
    Hash = defaultdict ( lambda : 0 )
    for i in range ( 0 , n ) :
        Hash [ A [ i ] ] += 1
        Hash [ B [ i ] ] += 1
    Sum = 0
    for x in Hash :
        if Hash [ x ] == 1 :
            Sum += x
    return Sum

PAIR_WITH_GIVEN_PRODUCT_SET_1_FIND_IF_ANY_PAIR_EXISTS_1 | def isProduct ( arr , n , x ) :
    if n < 2 :
        return False
    s = set ( )
    for i in range ( 0 , n ) :
        if arr [ i ] == 0 :
            if x == 0 :
                return True
            else :
                continue
        if x % arr [ i ] == 0 :
            if x // arr [ i ] in s :
                return True
            s.add ( arr [ i ] )
    return False

PANGRAM_CHECKING | def checkPangram ( s ) :
    List = [ ]
    for i in range ( 26 ) :
        List.append ( False )
    for c in s :
        if 'A' <= c and c <= 'Z':
            List [ ord ( c ) - ord ( 'A' ) ] = True
        elif 'a' <= c and c <= 'z':
            List [ ord ( c ) - ord ( 'a' ) ] = True
    for ch in List :
        if ch == False :
            return False
    return True

PAPER_CUT_MINIMUM_NUMBER_SQUARES | def minimumSquare ( a , b ) :
    result = 0
    rem = 0
    if ( a < b ) :
        a , b = b , a
    while ( b > 0 ) :
        result += int ( a / b )
        rem = int ( a % b )
        a = b
        b = rem
    return result

PARTITION_INTO_TWO_SUBARRAYS_OF_LENGTHS_K_AND_N_K_SUCH_THAT_THE_DIFFERENCE_OF_SUMS_IS_MAXIMUM | def maxDifference ( arr , N , k ) :
    S = 0
    S1 = 0
    max_difference = 0
    for i in range ( N ) :
        S += arr [ i ]
    arr.sort ( reverse = True )
    M = max ( k , N - k )
    for i in range ( M ) :
        S1 += arr [ i ]
    max_difference = S1 - ( S - S1 )
    return max_difference

PATH_MAXIMUM_AVERAGE_VALUE | def maxAverageOfPath ( cost , N ) :
    dp = [ [ 0 for i in range ( N + 1 ) ] for j in range ( N + 1 ) ]
    dp [ 0 ] [ 0 ] = cost [ 0 ] [ 0 ]
    for i in range ( 1 , N ) :
        dp [ i ] [ 0 ] = dp [ i - 1 ] [ 0 ] + cost [ i ] [ 0 ]
    for j in range ( 1 , N ) :
        dp [ 0 ] [ j ] = dp [ 0 ] [ j - 1 ] + cost [ 0 ] [ j ]
    for i in range ( 1 , N ) :
        for j in range ( 1 , N ) :
            dp [ i ] [ j ] = max ( dp [ i - 1 ] [ j ] , dp [ i ] [ j - 1 ] ) + cost [ i ] [ j ]
    return dp [ N - 1 ] [ N - 1 ] / ( 2 * N - 1 )

PERMUTE_TWO_ARRAYS_SUM_EVERY_PAIR_GREATER_EQUAL_K | def isPossible ( a , b , n , k ) :
    a = a [ : n ]
    b = b [ : n ]
    a.sort ( reverse = True )
    b.sort ( )
    for i in range ( n ) :
        if ( a [ i ] + b [ i ] < k ) :
            return False
    return True

PIZZA_CUT_PROBLEM_CIRCLE_DIVISION_LINES | def findMaximumPieces ( n ) :
    return int ( 1 + n * ( n + 1 ) / 2 )

POINT_CLIPPING_ALGORITHM_COMPUTER_GRAPHICS | def pointClip ( XY , n , Xmin , Ymin , Xmax , Ymax ) :
    print ( "Point inside the viewing pane:" )
    for i in range ( n ) :
        if ( ( XY [ i ] [ 0 ] >= Xmin ) and ( XY [ i ] [ 0 ] <= Xmax ) ) :
            if ( ( XY [ i ] [ 1 ] >= Ymin ) and ( XY [ i ] [ 1 ] <= Ymax ) ) :
                print ( "[" , XY [ i ] [ 0 ] , ", " , XY [ i ] [ 1 ] , "]" , sep = "" , end = "" )
    print ( "\n\nPoint outside the viewing pane:" )
    for i in range ( n ) :
        if ( ( XY [ i ] [ 0 ] < Xmin ) or ( XY [ i ] [ 0 ] > Xmax ) ) :
            print ( "[" , XY [ i ] [ 0 ] , ", " , XY [ i ] [ 1 ] , "]" , sep = "" , end = "" )
        if ( ( XY [ i ] [ 1 ] < Ymin ) or ( XY [ i ] [ 1 ] > Ymax ) ) :
            print ( "[" , XY [ i ] [ 0 ] , ", " , XY [ i ] [ 1 ] , "]" , sep = "" , end = "" )

POSITIVE_ELEMENTS_EVEN_NEGATIVE_ODD_POSITIONS | def rearrange ( a , size ) :
    positive = 0
    negative = 1
    while ( True ) :
        while ( positive < size and a [ positive ] >= 0 ) :
            positive = positive + 2
        while ( negative < size and a [ negative ] <= 0 ) :
            negative = negative + 2
        if ( positive < size and negative < size ) :
            temp = a [ positive ]
            a [ positive ] = a [ negative ]
            a [ negative ] = temp
        else :
            break

POSSIBLE_FORM_TRIANGLE_ARRAY_VALUES | def isPossibleTriangle ( arr , N ) :
    arr = arr [ : N ]
    if N < 3 :
        return False
    arr.sort ( )
    for i in range ( N - 2 ) :
        if arr [ i ] + arr [ i + 1 ] > arr [ i + 2 ] :
            return True
    return False

PRIMALITY_TEST_SET_1_INTRODUCTION_AND_SCHOOL_METHOD_1 | def isPrime ( n ) :
    if ( n <= 1 ) :
        return False
    if ( n <= 3 ) :
        return True
    if ( n % 2 == 0 or n % 3 == 0 ) :
        return False
    i = 5
    while ( i * i <= n ) :
        if ( n % i == 0 or n % ( i + 2 ) == 0 ) :
            return False
        i = i + 6
    return True

PRIMALITY_TEST_SET_5USING_LUCAS_LEHMER_SERIES | def isPrime ( p ) :
    checkNumber = 2 ** p - 1
    nextval = 4 % checkNumber
    for i in range ( 1 , p - 1 ) :
        nextval = ( nextval * nextval - 2 ) % checkNumber
    if ( nextval == 0 ) : return True
    else : return False

PRIME_NUMBERS | def isPrime ( n ) :
    if ( n <= 1 ) :
        return False
    for i in range ( 2 , n ) :
        if ( n % i == 0 ) :
            return False
    return True

PRINT_A_CLOSEST_STRING_THAT_DOES_NOT_CONTAIN_ADJACENT_DUPLICATES | def noAdjacentDup ( s ) :
    n = len ( s )
    for i in range ( 1 , n ) :
        if ( s [ i ] == s [ i - 1 ] ) :
            s [ i ] = "a"
            while ( s [ i ] == s [ i - 1 ] or ( i + 1 < n and s [ i ] == s [ i + 1 ] ) ) :
                s [ i ] += 1
            i += 1
    return s

PRINT_MATRIX_ANTISPIRAL_FORM | def antiSpiralTraversal ( m , n , a ) :
    k = 0
    l = 0
    stk = [ ]
    while ( k <= m and l <= n ) :
        for i in range ( l , n + 1 ) :
            stk.append ( a [ k ] [ i ] )
        k += 1
        for i in range ( k , m + 1 ) :
            stk.append ( a [ i ] [ n ] )
        n -= 1
        if ( k <= m ) :
            for i in range ( n , l - 1 , - 1 ) :
                stk.append ( a [ m ] [ i ] )
            m -= 1
        if ( l <= n ) :
            for i in range ( m , k - 1 , - 1 ) :
                stk.append ( a [ i ] [ l ] )
            l += 1
    while len ( stk ) != 0 :
        print ( str ( stk [ - 1 ] ) , end = " " )
        stk.pop ( )

PRINT_MATRIX_SPIRAL_FORM_STARTING_POINT | def printSpiral ( mat , r , c ) :
    a = 0
    b = 2
    low_row = 0 if ( 0 > a ) else a
    low_column = 0 if ( 0 > b ) else b - 1
    high_row = r - 1 if ( ( a + 1 ) >= r ) else a + 1
    high_column = c - 1 if ( ( b + 1 ) >= c ) else b + 1
    while ( ( low_row > 0 - r and low_column > 0 - c ) ) :
        i = low_column + 1
        while ( i <= high_column and i < c and low_row >= 0 ) :
            print ( mat [ low_row ] [ i ] , end = " " )
            i += 1
        low_row -= 1
        i = low_row + 2
        while ( i <= high_row and i < r and high_column < c ) :
            print ( mat [ i ] [ high_column ] , end = " " )
            i += 1
        high_column += 1
        i = high_column - 2
        while ( i >= low_column and i >= 0 and high_row < r ) :
            print ( mat [ high_row ] [ i ] , end = " " )
            i -= 1
        high_row += 1
        i = high_row - 2
        while ( i > low_row and i >= 0 and low_column >= 0 ) :
            print ( mat [ i ] [ low_column ] , end = " " )
            i -= 1
        low_column -= 1
    print ( )

PRINT_MAXIMUM_SHORTEST_DISTANCE | def find_maximum ( a , n , k ) :
    b = dict ( )
    for i in range ( n ) :
        x = a [ i ]
        d = min ( 1 + i , n - i )
        if x not in b.keys ( ) :
            b [ x ] = d
        else :
            b [ x ] = min ( d , b [ x ] )
    ans = sys.maxsize
    for i in range ( n ) :
        x = a [ i ]
        if ( x != ( k - x ) and ( k - x ) in b.keys ( ) ) :
            ans = min ( max ( b [ x ] , b [ k - x ] ) , ans )
    return ans

PROBABILITY_THREE_RANDOMLY_CHOSEN_NUMBERS_AP | def procal ( n ) :
    return ( 3.0 * n ) / ( 4.0 * ( n * n ) - 1 )

PROGRAMMING_PUZZLE_ASSIGN_VALUE_WITHOUT_CONTROL_STATEMENT | def assignValue ( a , b , x ) :
    arr = [ a , b ]
    return ( arr [ x ] )

PROGRAM_AREA_SQUARE | def areaSquare ( side ) :
    area = side * side
    return area

PROGRAM_BEST_FIT_ALGORITHM_MEMORY_MANAGEMENT | def bestFit ( blockSize , m , processSize , n ) :
    allocation = [ - 1 ] * n
    for i in range ( n ) :
        bestIdx = - 1
        for j in range ( m ) :
            if blockSize [ j ] >= processSize [ i ] :
                if bestIdx == - 1 :
                    bestIdx = j
                elif blockSize [ bestIdx ] > blockSize [ j ] :
                    bestIdx = j
        if bestIdx != - 1 :
            allocation [ i ] = bestIdx
            blockSize [ bestIdx ] -= processSize [ i ]
    print ( "Process No.Process Size     Block no." )
    for i in range ( n ) :
        print ( i + 1 , "         " , processSize [ i ] , end = "         " )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )

PROGRAM_BINARY_DECIMAL_CONVERSION_1 | def binaryToDecimal ( n ) :
    num = n
    dec_value = 0
    base1 = 1
    len1 = len ( num )
    for i in range ( len1 - 1 , - 1 , - 1 ) :
        if ( num [ i ] == '1' ) :
            dec_value += base1
        base1 = base1 * 2
    return dec_value

PROGRAM_CALCULATE_AREA_OCTAGON | def areaOctagon ( side ) :
    return ( 2 * ( 1 + ( math.sqrt ( 2 ) ) ) * side * side )

PROGRAM_CALCULATE_VOLUME_ELLIPSOID | def volumeOfEllipsoid(r1, r2, r3):
    pi = 3.14
    return 1.33 * pi * r1 * r2 * r3

PROGRAM_CALCULATE_VOLUME_OCTAHEDRON | def vol_of_octahedron ( side ) :
    return ( ( side * side * side ) * ( math.sqrt ( 2 ) / 3 ) )

PROGRAM_CENSOR_WORD_ASTERISKS_SENTENCE | def censor ( text , word ) :
    word_list = text.split ( )
    result = ''
    stars = '*' * len ( word )
    count = 0
    index = 0
    for i in word_list :
        if i == word :
            word_list [ index ] = stars
        index += 1
    result = ' '.join ( word_list )
    return result

PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE_1 | def arraySortedOrNot ( arr , n ) :
    if ( n == 0 or n == 1 ) :
        return True
    for i in range ( 1 , n ) :
        if ( arr [ i - 1 ] > arr [ i ] ) :
            return False
    return True

PROGRAM_CHECK_INPUT_INTEGER_STRING | def isNumber ( s ) :
    for i in range ( len ( s ) ) :
        if s [ i ].isdigit ( ) != True :
            return False
    return True

PROGRAM_CHECK_ISBN | def isValidISBN ( isbn ) :
    if len ( isbn ) != 10 :
        return False
    _sum = 0
    for i in range ( 9 ) :
        if 0 <= int ( isbn [ i ] ) <= 9 :
            _sum += int ( isbn [ i ] ) * ( 10 - i )
        else :
            return False
    if ( isbn [ 9 ] != 'X' and 0 <= int ( isbn [ 9 ] ) <= 9 ) :
        return False
    _sum += 10 if isbn [ 9 ] == 'X' else int ( isbn [ 9 ] )
    return ( _sum % 11 == 0 )

PROGRAM_COUNT_OCCURRENCE_GIVEN_CHARACTER_STRING | def count ( s , c ) :
    res = 0
    for i in range ( len ( s ) ) :
        if ( s [ i ] == c ) :
            res = res + 1
    return res

PROGRAM_DECIMAL_BINARY_CONVERSION_2 | def decimalToBinary ( N ) :
    B_Number = 0
    cnt = 0
    while ( N != 0 ) :
        rem = N % 2
        c = pow ( 10 , cnt )
        B_Number += rem * c
        N //= 2
        cnt += 1
    return B_Number

PROGRAM_DISTANCE_TWO_POINTS_EARTH | def distance ( lat1 , lat2 , lon1 , lon2 ) :
    lon1 = radians ( lon1 )
    lon2 = radians ( lon2 )
    lat1 = radians ( lat1 )
    lat2 = radians ( lat2 )
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin ( dlat / 2 ) ** 2 + cos ( lat1 ) * cos ( lat2 ) * sin ( dlon / 2 ) ** 2
    c = 2 * asin ( sqrt ( a ) )
    r = 6371
    return ( c * r )

PROGRAM_FIND_CIRCUMFERENCE_CIRCLE | def circumference ( r ) :
    pi = 3.1415
    return ( 2 * pi * r )

PROGRAM_FIND_REMAINDER_LARGE_NUMBER_DIVIDED_11 | def remainder ( str ) :
    ln = len ( str )
    rem = 0
    for i in range ( 0 , ln ) :
        num = rem * 10 + ( int ) ( str [ i ] )
        rem = num % 11
    return rem

PROGRAM_FIND_SLOPE_LINE | def slope ( x1 , y1 , x2 , y2 ) :
    return ( float ) ( y2 - y1 ) / ( x2 - x1 )

PROGRAM_FIND_SMALLEST_DIFFERENCE_ANGLES_TWO_PARTS_GIVEN_CIRCLE | def findMinimumAngle ( arr , n ) :
    l = 0
    _sum = 0
    ans = 360
    for i in range ( n ) :
        _sum += arr [ i ]
        while _sum >= 180 :
            ans = min ( ans , 2 * abs ( 180 - _sum ) )
            _sum -= arr [ l ]
            l += 1
        ans = min ( ans , 2 * abs ( 180 - _sum ) )
    return ans

PROGRAM_FIND_STRING_START_END_GEEKS | def isCornerPresent ( str , corner ) :
    n = len ( str )
    cl = len ( corner )
    if ( n < cl ) :
        return False
    return ( ( str [ : cl ] == corner ) and ( str [ n - cl : ] == corner ) )

PROGRAM_FOR_DEADLOCK_FREE_CONDITION_IN_OPERATING_SYSTEM | def Resources ( process , need ) :
    minResources = 0
    minResources = process * ( need - 1 ) + 1
    return minResources

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER | def factorial ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * factorial ( n - 1 )

PROGRAM_FOR_FACTORIAL_OF_A_NUMBER_1 | def factorial ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * factorial ( n - 1 )

PROGRAM_FOR_SURFACE_AREA_OF_OCTAHEDRON | def surface_area_octahedron ( side ) :
    return ( 2 * ( math.sqrt ( 3 ) ) * ( side * side ) )

PROGRAM_OCTAL_DECIMAL_CONVERSION | def octalToDecimal ( n ) :
    num = n
    dec_value = 0
    base = 1
    temp = num
    while ( temp ) :
        last_digit = temp % 10
        temp = int ( temp / 10 )
        dec_value += last_digit * base
        base = base * 8
    return dec_value

PROGRAM_PRINT_IDENTITY_MATRIX_1 | def isIdentity ( mat , N ) :
    for row in range ( N ) :
        for col in range ( N ) :
            if ( row == col and mat [ row ] [ col ] != 1 ) :
                return False
            elif ( row != col and mat [ row ] [ col ] != 0 ) :
                return False
    return True

PROGRAM_PRINT_SUM_GIVEN_NTH_TERM_1 | def summingSeries ( n ) :
    return int ( math.pow ( n , 2 ) )

PROGRAM_REVERSE_STRING_ITERATIVE_RECURSIVE | def recursiveReverse ( str ) :
    stack = [ ]
    for i in range ( len ( str ) ) :
        stack.append ( str [ i ] )
    for i in range ( len ( str ) ) :
        str [ i ] = stack.pop ( )

PROGRAM_TO_CHECK_IF_A_GIVEN_NUMBER_IS_LUCKY_ALL_DIGITS_ARE_DIFFERENT | def isLucky ( n ) :
    ar = [ 0 ] * 10
    while ( n > 0 ) :
        digit = math.floor ( n % 10 )
        if ( ar [ digit ] ) :
            return False
        ar [ digit ] = 1
        n = int ( n / 10 )
    return True

PROGRAM_TO_CHECK_IF_A_MATRIX_IS_SYMMETRIC | def isSymmetric ( mat , N ) :
    for i in range ( N ) :
        for j in range ( N ) :
            if ( mat [ i ] [ j ] != mat [ j ] [ i ] ) :
                return False
    return True

PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR | def getRemainder ( num , divisor ) :
    return ( num - divisor * ( num // divisor ) )

PROGRAM_TO_FIND_THE_AREA_OF_PENTAGON | def findArea ( a ) :
    area = ( sqrt ( 5 * ( 5 + 2 * ( sqrt ( 5 ) ) ) ) * a * a ) / 4
    return area

PROGRAM_WORST_FIT_ALGORITHM_MEMORY_MANAGEMENT | def worstFit ( blockSize , m , processSize , n ) :
    allocation = [ - 1 ] * n
    for i in range ( n ) :
        wstIdx = - 1
        for j in range ( m ) :
            if blockSize [ j ] >= processSize [ i ] :
                if wstIdx == - 1 :
                    wstIdx = j
                elif blockSize [ wstIdx ] < blockSize [ j ] :
                    wstIdx = j
        if wstIdx != - 1 :
            allocation [ i ] = wstIdx
            blockSize [ wstIdx ] -= processSize [ i ]
    print ( "Process No.Process Size Block no." )
    for i in range ( n ) :
        print ( i + 1 , "         " , processSize [ i ] , end = "     " )
        if allocation [ i ] != - 1 :
            print ( allocation [ i ] + 1 )
        else :
            print ( "Not Allocated" )

PYTHON_PROGRAM_FIND_PERIMETER_CIRCUMFERENCE_SQUARE_RECTANGLE | def Circumference ( a ) :
    return ( 4 * a )

QUERIES_COUNTS_ARRAY_ELEMENTS_VALUES_GIVEN_RANGE | def countInRange ( arr , n , x , y ) :
    count = 0 ;
    for i in range ( n ) :
        if ( arr [ i ] >= x and arr [ i ] <= y ) :
            count += 1
    return count

QUICK_WAY_CHECK_CHARACTERS_STRING | def allCharactersSame ( s ) :
    n = len ( s )
    for i in range ( 1 , n ) :
        if s [ i ] != s [ 0 ] :
            return False
    return True

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM | def rearrange ( arr , n ) :
    temp = n * [ None ]
    small , large = 0 , n - 1
    flag = True
    for i in range ( n ) :
        if flag is True :
            temp [ i ] = arr [ large ]
            large -= 1
        else :
            temp [ i ] = arr [ small ]
            small += 1
        flag = bool ( 1 - flag )
    for i in range ( n ) :
        arr [ i ] = temp [ i ]
    return arr

REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM_SET_2_O1_EXTRA_SPACE | def rearrange ( arr , n ) :
    max_idx = n - 1
    min_idx = 0
    max_elem = arr [ n - 1 ] + 1
    for i in range ( 0 , n ) :
        if i % 2 == 0 :
            arr [ i ] += ( arr [ max_idx ] % max_elem ) * max_elem
            max_idx -= 1
        else :
            arr [ i ] += ( arr [ min_idx ] % max_elem ) * max_elem
            min_idx += 1
    for i in range ( 0 , n ) :
        arr [ i ] = int ( arr [ i ] / max_elem )

REARRANGE_POSITIVE_AND_NEGATIVE_NUMBERS_PUBLISH | def rearrange ( arr , n ) :
    i = - 1
    for j in range ( n ) :
        if ( arr [ j ] < 0 ) :
            i += 1
            arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
    pos , neg = i + 1 , 0
    while ( pos < n and neg < pos and arr [ neg ] < 0 ) :
        arr [ neg ] , arr [ pos ] = arr [ pos ] , arr [ neg ]
        pos += 1
        neg += 2

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM | def breakSum ( n ) :
    if ( n == 0 or n == 1 ) :
        return n
    return max ( ( breakSum ( n // 2 ) + breakSum ( n // 3 ) + breakSum ( n // 4 ) ) , n )

RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM_1 | def breakSum ( n ) :
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = 0
    dp [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        dp [ i ] = max ( dp [ int ( i / 2 ) ] + dp [ int ( i / 3 ) ] + dp [ int ( i / 4 ) ] , i )
    return dp [ n ]

RECURSIVE_C_PROGRAM_LINEARLY_SEARCH_ELEMENT_GIVEN_ARRAY | def recSearch ( arr , l , r , x ) :
    if r < l :
        return - 1
    if arr [ l ] == x :
        return l
    if arr [ r ] == x :
        return r
    return recSearch ( arr , l + 1 , r - 1 , x )

RECURSIVE_INSERTION_SORT | def insertionSortRecursive ( arr , n ) :
    if n <= 1 :
        return
    insertionSortRecursive ( arr , n - 1 )
    last = arr [ n - 1 ]
    j = n - 2
    while ( j >= 0 and arr [ j ] > last ) :
        arr [ j + 1 ] = arr [ j ]
        j = j - 1
    arr [ j + 1 ] = last

RECURSIVE_PROGRAM_PRIME_NUMBER | def isPrime ( n , i = 2 ) :
    if ( n <= 2 ) :
        return True if ( n == 2 ) else False
    if ( n % i == 0 ) :
        return False
    if ( i * i > n ) :
        return true
    return isPrime ( n , i + 1 )

REMAINDER_7_LARGE_NUMBERS | def remainderWith7 ( num ) :
    series = [ 1 , 3 , 2 , - 1 , - 3 , - 2 ]
    series_index = 0
    result = 0
    for i in range ( ( len ( num ) - 1 ) , - 1 , - 1 ) :
        digit = ord ( num [ i ] ) - 48
        result += digit * series [ series_index ]
        series_index = ( series_index + 1 ) % 6
        result %= 7
    if ( result < 0 ) :
        result = ( result + 7 ) % 7
    return result

REMOVE_ARRAY_END_ELEMENT_MAXIMIZE_SUM_PRODUCT | def solve ( dp , a , low , high , turn ) :
    if ( low == high ) :
        return a [ low ] * turn
    if ( dp [ low ] [ high ] != 0 ) :
        return dp [ low ] [ high ]
    dp [ low ] [ high ] = max ( a [ low ] * turn + solve ( dp , a , low + 1 , high , turn + 1 ) , a [ high ] * turn + solve ( dp , a , low , high - 1 , turn + 1 ) ) ;
    return dp [ low ] [ high ]

REMOVE_BRACKETS_ALGEBRAIC_STRING_CONTAINING_OPERATORS | def simplify ( Str ) :
    Len = len ( Str )
    res = [ None ] * Len
    index = 0
    i = 0
    s = [ ]
    s.append ( 0 )
    while ( i < Len ) :
        if ( Str [ i ] == '+' ) :
            if ( s [ - 1 ] == 1 ) :
                res [ index ] = '-'
                index += 1
            if ( s [ - 1 ] == 0 ) :
                res [ index ] = '+'
                index += 1
        elif ( Str [ i ] == '-' ) :
            if ( s [ - 1 ] == 1 ) :
                res [ index ] = '+'
                index += 1
            elif ( s [ - 1 ] == 0 ) :
                res [ index ] = '-'
                index += 1
        elif ( Str [ i ] == '(' and i > 0 ) :
            if ( Str [ i - 1 ] == '-' ) :
                x = 0 if ( s [ - 1 ] == 1 ) else 1
                s.append ( x )
            elif ( Str [ i - 1 ] == '+' ) :
                s.append ( s [ - 1 ] )
        elif ( Str [ i ] == ')' ) :
            s.pop ( )
        else :
            res [ index ] = Str [ i ]
            index += 1
        i += 1
    return "".join(res)

REMOVE_CONSECUTIVE_DUPLICATES_STRING | def removeDuplicates ( S ) :
    n = len ( S )
    if ( n < 2 ) :
        return
    j = 0
    for i in range ( 1 , n ) :
        if ( S [ j ] != S [ i ] ) :
            j += 1
            S [ j ] = S [ i ]
    j += 1
    S = S [ : j ]

REMOVE_MINIMUM_ELEMENTS_EITHER_SIDE_2MIN_MAX | def minRemovalsDP ( arr , n ) :
    longest_start = - 1
    longest_end = 0
    for start in range ( n ) :
        min = sys.maxsize
        max = - sys.maxsize
        for end in range ( start , n ) :
            val = arr [ end ]
            if ( val < min ) :
                min = val
            if ( val > max ) :
                max = val
            if ( 2 * min <= max ) :
                break
            if ( end - start > longest_end - longest_start or longest_start == - 1 ) :
                longest_start = start
                longest_end = end
    if ( longest_start == - 1 ) :
        return n
    return ( n - ( longest_end - longest_start + 1 ) )

REPLACE_CHARACTER_C1_C2_C2_C1_STRING_S | def replace ( s , c1 , c2 ) :
    l = len ( s )
    for i in range ( l ) :
        if ( s [ i ] == c1 ) :
            s = s [ 0 : i ] + c2 + s [ i + 1 : ]
        elif ( s [ i ] == c2 ) :
            s = s [ 0 : i ] + c1 + s [ i + 1 : ]
    return s

ROW_WISE_COMMON_ELEMENTS_TWO_DIAGONALS_SQUARE_MATRIX | def countCommon ( mat , n ) :
    res = 0
    for i in range ( n ) :
        if mat [ i ] [ i ] == mat [ i ] [ n - i - 1 ] :
            res = res + 1
    return res

SEARCHING_ARRAY_ADJACENT_DIFFER_K | def search ( arr , n , x , k ) :
    i = 0
    while ( i < n ) :
        if ( arr [ i ] == x ) :
            return i
        i = i + max ( 1 , int ( abs ( arr [ i ] - x ) / k ) )
    print ( "number is not present!" )
    return - 1

SEARCH_ALMOST_SORTED_ARRAY | def binarySearch ( arr , l , r , x ) :
    if ( r >= l ) :
        mid = int ( l + ( r - l ) / 2 )
        if ( arr [ mid ] == x ) : return mid
        if ( mid > l and arr [ mid - 1 ] == x ) :
            return ( mid - 1 )
        if ( mid < r and arr [ mid + 1 ] == x ) :
            return ( mid + 1 )
        if ( arr [ mid ] > x ) :
            return binarySearch ( arr , l , mid - 2 , x )
        return binarySearch ( arr , mid + 2 , r , x )
    return - 1

SEARCH_AN_ELEMENT_IN_AN_ARRAY_WHERE_DIFFERENCE_BETWEEN_ADJACENT_ELEMENTS_IS_1 | def search ( arr , n , x ) :
    i = 0
    while ( i < n ) :
        if ( arr [ i ] == x ) :
            return i
        i = i + abs ( arr [ i ] - x )
    print ( "number is not present!" )
    return - 1

SEARCH_AN_ELEMENT_IN_A_SORTED_AND_PIVOTED_ARRAY | def search ( arr , l , h , key ) :
    if l > h :
        return - 1
    mid = ( l + h ) // 2
    if arr [ mid ] == key :
        return mid
    if arr [ l ] <= arr [ mid ] :
        if key >= arr [ l ] and key <= arr [ mid ] :
            return search ( arr , l , mid - 1 , key )
        return search ( arr , mid + 1 , h , key )
    if key >= arr [ mid ] and key <= arr [ h ] :
        return search ( arr , mid + 1 , h , key )
    return search ( arr , l , mid - 1 , key )

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY | def binarySearch ( arr , low , high , key ) :
    if ( high < low ) :
        return - 1
    mid = ( low + high ) / 2
    if ( key == arr [ int ( mid ) ] ) :
        return mid
    if ( key > arr [ int ( mid ) ] ) :
        return binarySearch ( arr , ( mid + 1 ) , high , key )
    return ( binarySearch ( arr , low , ( mid - 1 ) , key ) )

SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY_1 | def insertSorted ( arr , n , key , capacity ) :
    if ( n >= capacity ) :
        return n
    i = n - 1
    while i >= 0 and arr [ i ] > key :
        arr [ i + 1 ] = arr [ i ]
        i -= 1
    arr [ i + 1 ] = key
    return ( n + 1 )

SEGREGATE_EVEN_ODD_NUMBERS_SET_3 | def arrayEvenAndOdd ( arr , n ) :
    i = - 1
    j = 0
    while ( j != n ) :
        if ( arr [ j ] % 2 == 0 ) :
            i = i + 1
            arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
        j = j + 1
    for i in arr :
        print ( str ( i ) + " " , end = '' )

SELECT_A_RANDOM_NUMBER_FROM_STREAM_WITH_O1_SPACE | def selectRandom ( x ) :
    res = 0
    count = 0
    count += 1
    if ( count == 1 ) :
        res = x
    else :
        i = random.randrange ( count )
        if ( i == count - 1 ) :
            res = x
    return res

SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS_1 | def getTotalNumberOfSequences ( m , n ) :
    T = [ [ 0 for i in range ( n + 1 ) ] for i in range ( m + 1 ) ]
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if i == 0 or j == 0 :
                T [ i ] [ j ] = 0
            elif i < j :
                T [ i ] [ j ] = 0
            elif j == 1 :
                T [ i ] [ j ] = i
            else :
                T [ i ] [ j ] = T [ i - 1 ] [ j ] + T [ i // 2 ] [ j - 1 ]
    return T [ m ] [ n ]

SHUFFLE_A_GIVEN_ARRAY | def randomize ( arr , n ) :
    for i in range ( n - 1 , 0 , - 1 ) :
        j = random.randint ( 0 , i + 1 )
        arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
    return arr

SIZE_SUBARRAY_MAXIMUM_SUM | def maxSubArraySum ( a , size ) :
    max_so_far = - maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range ( 0 , size ) :
        max_ending_here += a [ i ]
        if max_so_far < max_ending_here :
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0 :
            max_ending_here = 0
            s = i + 1
    return ( end - start + 1 )

SMALLEST_DIFFERENCE_PAIR_VALUES_TWO_UNSORTED_ARRAYS | def findSmallestDifference ( A , B , m , n ) :
    A = A [ : m ]
    B = B [ : n ]
    A.sort ( )
    B.sort ( )
    a = 0
    b = 0
    result = sys.maxsize
    while ( a < m and b < n ) :
        if ( abs ( A [ a ] - B [ b ] ) < result ) :
            result = abs ( A [ a ] - B [ b ] )
        if ( A [ a ] < B [ b ] ) :
            a += 1
        else :
            b += 1
    return result

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS | def smallest ( x , y , z ) :
    c = 0
    while ( x and y and z ) :
        x = x - 1
        y = y - 1
        z = z - 1
        c = c + 1
    return c

SMALLEST_OF_THREE_INTEGERS_WITHOUT_COMPARISON_OPERATORS_1 | def smallest ( x , y , z ) :
    if ( not int ( y / x ) ) :
        return y if ( not int ( y / z ) ) else z
    return x if ( not int ( x / z ) ) else z

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_1 | def nextPowerOf2 ( n ) :
    p = 1
    if ( n and not ( n & ( n - 1 ) ) ) :
        return n
    while ( p < n ) :
        p <<= 1
    return p

SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N_2 | def nextPowerOf2 ( n ) :
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n

SORT_AN_ARRAY_OF_0S_1S_AND_2S | def sort012 ( a , arr_size ) :
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi :
        if a [ mid ] == 0 :
            a [ lo ] , a [ mid ] = a [ mid ] , a [ lo ]
            lo = lo + 1
            mid = mid + 1
        elif a [ mid ] == 1 :
            mid = mid + 1
        else :
            a [ mid ] , a [ hi ] = a [ hi ] , a [ mid ]
            hi = hi - 1

SORT_ARRAY_APPLYING_GIVEN_EQUATION | def sortArray ( arr , n , A , B , C ) :
    for i in range ( n ) :
        arr [ i ] = ( A * arr [ i ] * arr [ i ] + B * arr [ i ] + C )
    index = - ( sys.maxsize - 1 )
    maximum = - ( sys.maxsize - 1 )
    for i in range ( n ) :
        if maximum < arr [ i ] :
            index = i
            maximum = arr [ i ]
    i = 0
    j = n - 1
    new_arr = [ 0 ] * n
    k = 0
    while i < index and j > index :
        if arr [ i ] < arr [ j ] :
            new_arr [ k ] = arr [ i ]
            k += 1
            i += 1
        else :
            new_arr [ k ] = arr [ j ]
            k += 1
            j -= 1
    while i < index :
        new_arr [ k ] = arr [ i ]
        k += 1
        i += 1
    while j > index :
        new_arr [ k ] = arr [ j ]
        k += 1
        j -= 1
        new_arr [ n - 1 ] = maximum
    for i in range ( n ) :
        arr [ i ] = new_arr [ i ]

SORT_ARRAY_CONTAIN_1_N_VALUES | def sortit ( arr , n ) :
    for i in range ( n ) :
        arr [ i ] = i + 1

SORT_ARRAY_TWO_HALVES_SORTED | def mergeTwoHalf ( A , n ) :
    A.sort ( )

SORT_ARRAY_WAVE_FORM_2_1 | def sortInWave ( arr , n ) :
    for i in range ( 0 , n , 2 ) :
        if ( i > 0 and arr [ i ] < arr [ i - 1 ] ) :
            arr [ i ] , arr [ i - 1 ] = arr [ i - 1 ] , arr [ i ]
        if ( i < n - 1 and arr [ i ] < arr [ i + 1 ] ) :
            arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i ]

SORT_EVEN_NUMBERS_ASCENDING_ORDER_SORT_ODD_NUMBERS_DESCENDING_ORDER_1 | def twoWaySort ( arr , n ) :
    for i in range ( 0 , n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1
    arr.sort ( )
    for i in range ( 0 , n ) :
        if ( arr [ i ] & 1 ) :
            arr [ i ] *= - 1

SORT_EVEN_PLACED_ELEMENTS_INCREASING_ODD_PLACED_DECREASING_ORDER | def bitonicGenerator ( arr , n ) :
    evenArr = [ ]
    oddArr = [ ]
    for i in range ( n ) :
        if ( ( i % 2 ) == 0 ) :
            evenArr.append ( arr [ i ] )
        else :
            oddArr.append ( arr [ i ] )
    evenArr = sorted ( evenArr )
    oddArr = sorted ( oddArr )
    oddArr = oddArr [ : : - 1 ]
    i = 0
    for j in range ( len ( evenArr ) ) :
        arr [ i ] = evenArr [ j ]
        i += 1
    for j in range ( len ( oddArr ) ) :
        arr [ i ] = oddArr [ j ]
        i += 1

SPACE_OPTIMIZED_DP_SOLUTION_0_1_KNAPSACK_PROBLEM | def KnapSack ( val , wt , n , W ) :
    mat = [ [ 0 for i in range ( W + 1 ) ] for i in range ( 2 ) ]
    i = 0
    while i < n :
        j = 0
        if i % 2 == 0 :
            while j < W :
                j += 1
                if wt [ i ] <= j and j - wt [ i ] < W:
                    mat [ 1 ] [ j ] = max ( val [ i ] + mat [ 0 ] [ j - wt [ i ] ] , mat [ 0 ] [ j ] )
                else :
                    mat [ 1 ] [ j ] = mat [ 0 ] [ j ]
        else :
            while j < W :
                j += 1
                if wt [ i ] <= j and j - wt [ i ] < W:
                    mat [ 0 ] [ j ] = max ( val [ i ] + mat [ 1 ] [ j - wt [ i ] ] , mat [ 1 ] [ j ] )
                else :
                    mat [ 0 ] [ j ] = mat [ 1 ] [ j ]
        i += 1
    if n % 2 == 0 :
        return mat [ 0 ] [ W ]
    else :
        return mat [ 1 ] [ W ]

SPACE_OPTIMIZED_DP_SOLUTION_0_1_KNAPSACK_PROBLEM_1 | def KnapSack ( val , wt , n , W ) :
    dp = [ 0 ] * ( W + 1 )
    for i in range ( n ) :
        for j in range ( W , -1 , - 1 ) :
            if j - wt [ i ] < W + 1 and j - wt [ i ] >= 0:
                dp [ j ] = max ( dp [ j ] , val [ i ] + dp [ j - wt [ i ] ] )
    return dp [ W ]

SPLIT_ARRAY_ADD_FIRST_PART_END | def splitArr ( arr , n , k ) :
    for i in range ( 0 , k ) :
        x = arr [ 0 ]
        for j in range ( 0 , n - 1 ) :
            arr [ j ] = arr [ j + 1 ]
        arr [ n - 1 ] = x

SQUARED_TRIANGULAR_NUMBER_SUM_CUBES | def findS ( s ) :
    _sum = 0
    n = 1
    while ( _sum < s ) :
        _sum += n * n * n
        n += 1
    n -= 1
    if _sum == s :
        return n
    return - 1

SQUARES_OF_MATRIX_DIAGONAL_ELEMENTS | def diagonalsquare ( mat , row , column ) :
    print ( "Diagonal one : " , end = "" )
    for i in range ( 0 , row ) :
        for j in range ( 0 , column ) :
            if ( i == j ) :
                print ( "{} ".format ( mat [ i ] [ j ] * mat [ i ] [ j ] ) , end = "" )
    print ( " \n\nDiagonal two : " , end = "" )
    for i in range ( 0 , row ) :
        for j in range ( 0 , column ) :
            if ( i + j == column - 1 ) :
                print ( "{} ".format ( mat [ i ] [ j ] * mat [ i ] [ j ] ) , end = "" )

SQUARE_PYRAMIDAL_NUMBER_SUM_SQUARES | def findS ( s ) :
    _sum = 0
    n = 1
    while ( _sum < s ) :
        _sum += n * n
        n += 1
    n -= 1
    if _sum == s :
        return n
    return - 1

SQUARE_ROOT_OF_AN_INTEGER | def floorSqrt ( x ) :
    if ( x == 0 or x == 1 ) :
        return x
    i = 1
    result = 1
    while ( result <= x ) :
        i += 1
        result = i * i
    return i - 1

SQUARE_ROOT_OF_A_PERFECT_SQUARE | def squareRoot ( n ) :
    x = n
    y = 1
    e = 0.000001
    while ( x - y > e ) :
        x = ( x + y ) / 2
        y = n / x
    return x

STACK_SET_3_REVERSE_STRING_USING_STACK | def reverse ( string ) :
    string = string [ : : - 1 ]
    return string

STEINS_ALGORITHM_FOR_FINDING_GCD | def gcd ( a , b ) :
    if ( a == 0 ) :
        return b
    if ( b == 0 ) :
        return a
    k = 0
    while ( ( ( a | b ) & 1 ) == 0 ) :
        a = a >> 1
        b = b >> 1
        k = k + 1
    while ( ( a & 1 ) == 0 ) :
        a = a >> 1
    while ( b != 0 ) :
        while ( ( b & 1 ) == 0 ) :
            b = b >> 1
        if ( a > b ) :
            temp = a
            a = b
            b = temp
        b = ( b - a )
    return ( a << k )

STEINS_ALGORITHM_FOR_FINDING_GCD_1 | def gcd ( a , b ) :
    if ( a == b ) :
        return a
    if ( a == 0 ) :
        return b
    if ( b == 0 ) :
        return a
    if ( ( ~ a & 1 ) == 1 ) :
        if ( ( b & 1 ) == 1 ) :
            return gcd ( a >> 1 , b )
        else :
            return ( gcd ( a >> 1 , b >> 1 ) << 1 )
    if ( ( ~ b & 1 ) == 1 ) :
        return gcd ( a , b >> 1 )
    if ( a > b ) :
        return gcd ( ( a - b ) >> 1 , b )
    return gcd ( ( b - a ) >> 1 , a )

STOOGE_SORT | def stoogesort ( arr , l , h ) :
    if l >= h :
        return
    if arr [ l ] > arr [ h ] :
        t = arr [ l ]
        arr [ l ] = arr [ h ]
        arr [ h ] = t
    if h - l + 1 > 2 :
        t = ( int ) ( ( h - l + 1 ) / 3 )
        stoogesort ( arr , l , ( h - t ) )
        stoogesort ( arr , l + t , ( h ) )
        stoogesort ( arr , l , ( h - t ) )

STRING_CONTAINING_FIRST_LETTER_EVERY_WORD_GIVEN_STRING_SPACES | def firstLetterWord ( str ) :
    result = ""
    v = True
    for i in range ( len ( str ) ) :
        if ( str [ i ] == ' ' ) :
            v = True
        elif ( str [ i ] != ' ' and v == True ) :
            result += ( str [ i ] )
            v = False
    return result

SUBARRAYS_DISTINCT_ELEMENTS | def sumoflength ( arr , n ) :
    s = [ ]
    j = 0
    ans = 0
    for i in range ( n ) :
        while ( j < n and ( arr [ j ] not in s ) ) :
            s.append ( arr [ j ] )
            j += 1
        ans += ( ( j - i ) * ( j - i + 1 ) ) // 2
        s.remove ( arr [ i ] )
    return ans

SUBSET_SUM_PROBLEM_OSUM_SPACE | def isSubsetSum ( arr , n , sum ) :
    subset = [ [ False for j in range ( sum + 1 ) ] for i in range ( 3 ) ]
    for i in range ( n + 1 ) :
        for j in range ( sum + 1 ) :
            if ( j == 0 ) :
                subset [ i % 2 ] [ j ] = True
            elif ( i == 0 ) :
                subset [ i % 2 ] [ j ] = False
            elif ( arr [ i - 1 ] <= j ) :
                subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j - arr [ i - 1 ] ] or subset [ ( i + 1 ) % 2 ] [ j ]
            else :
                subset [ i % 2 ] [ j ] = subset [ ( i + 1 ) % 2 ] [ j ]
    return subset [ n % 2 ] [ sum ]

SUM_AREA_RECTANGLES_POSSIBLE_ARRAY | def MaxTotalRectangleArea ( a , n ) :
    a = a [ : n ]
    a.sort (  )
    sum = 0
    flag = False
    len = 0
    i = 0
    while ( i < n - 1 ) :
        if ( ( a [ i ] == a [ i + 1 ] or a [ i ] - a [ i + 1 ] == 1 ) and flag == False ) :
            flag = True
            len = a [ i + 1 ]
            i = i + 1
        elif ( ( a [ i ] == a [ i + 1 ] or a [ i ] - a [ i + 1 ] == 1 ) and flag == True ) :
            sum = sum + a [ i + 1 ] * len
            flag = False
            i = i + 1
        i += 1
    return sum

SUM_BINOMIAL_COEFFICIENTS | def binomialCoeffSum ( n ) :
    C = [ [ 0 ] * ( n + 2 ) for i in range ( 0 , n + 2 ) ]
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , min ( i , n ) + 1 ) :
            if ( j == 0 or j == i ) :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ]
    sum = 0
    for i in range ( 0 , n + 1 ) :
        sum += C [ n ] [ i ]
    return sum

SUM_BINOMIAL_COEFFICIENTS_1 | def binomialCoeffSum ( n ) :
    return ( 1 << n )

SUM_DIVISORS_1_N_1 | def divisorSum ( n ) :
    sum = 0
    for i in range ( 1 , n + 1 ) :
        sum += int ( n / i ) * i
    return int ( sum )

SUM_FACTORS_NUMBER | def divSum ( n ) :
    result = 0
    for i in range ( 2 , ( int ) ( math.sqrt ( n ) ) + 1 ) :
        if ( n % i == 0 ) :
            if ( i == ( n / i ) ) :
                result = result + i
            else :
                result = result + ( i + n // i )
    return ( result + n + 1 )

SUM_FIBONACCI_NUMBERS | def calculateSum ( n ) :
    if ( n <= 0 ) :
        return 0
    fibo = [ 0 ] * ( n + 1 )
    fibo [ 1 ] = 1
    sm = fibo [ 0 ] + fibo [ 1 ]
    for i in range ( 2 , n + 1 ) :
        fibo [ i ] = fibo [ i - 1 ] + fibo [ i - 2 ]
        sm = sm + fibo [ i ]
    return sm

SUM_K_TH_GROUP_ODD_POSITIVE_NUMBERS | def kthgroupsum ( k ) :
    cur = int ( ( k * ( k - 1 ) ) + 1 )
    sum = 0
    while k :
        sum += cur
        cur += 2
        k = k - 1
    return sum

SUM_MANHATTAN_DISTANCES_PAIRS_POINTS | def distancesum ( x , y , n ) :
    sum = 0
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            sum += ( abs ( x [ i ] - x [ j ] ) + abs ( y [ i ] - y [ j ] ) )
    return sum

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS | def findSum ( n ) :
    arr = [ [ 0 for x in range ( n ) ] for y in range ( n ) ]
    for i in range ( n ) :
        for j in range ( n ) :
            arr [ i ] [ j ] = abs ( i - j )
    sum = 0
    for i in range ( n ) :
        for j in range ( n ) :
            sum += arr [ i ] [ j ]
    return sum

SUM_MATRIX_ELEMENT_ABSOLUTE_DIFFERENCE_ROW_COLUMN_NUMBERS_2 | def findSum ( n ) :
    n -= 1
    sum = 0
    sum += ( n * ( n + 1 ) ) / 2
    sum += ( n * ( n + 1 ) * ( 2 * n + 1 ) ) / 6
    return int ( sum )

SUM_MATRIX_ELEMENT_ELEMENT_INTEGER_DIVISION_ROW_COLUMN_1 | def findSum ( n ) :
    ans = 0
    temp = 0
    for i in range ( 1 , n + 1 ) :
        if temp < n :
            temp = i - 1
            num = 1
            while temp < n :
                if temp + i <= n :
                    ans += i * num
                else :
                    ans += ( n - temp ) * num
                temp += i
                num += 1
    return ans

SUM_MIDDLE_ROW_COLUMN_MATRIX | def middlesum ( mat , n ) :
    row_sum = 0
    col_sum = 0
    for i in range ( n ) :
        row_sum += mat [ n // 2 ] [ i ]
    print ( "Sum of middle row = " , row_sum )
    for i in range ( n ) :
        col_sum += mat [ i ] [ n // 2 ]
    print ( "Sum of middle column = " , col_sum )

SUM_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING | def sumAtKthLevel ( tree , k ) :
    level = - 1
    sum = 0
    n = len ( tree )
    for i in range ( n ) :
        if ( tree [ i ] == '(' ) :
            level += 1
        elif ( tree [ i ] == ')' ) :
            level -= 1
        else :
            if ( level == k ) :
                sum += ( ord ( tree [ i ] ) - ord ( '0' ) )
    return sum

SUM_OF_ALL_ELEMENTS_UP_TO_NTH_ROW_IN_A_PASCALS_TRIANGLE_1 | def calculateSum ( n ) :
    sum = 0
    sum = 1 << n
    return ( sum - 1 )

SUM_OF_ALL_SUBSTRINGS_OF_A_STRING_REPRESENTING_A_NUMBER | def sumOfSubstrings ( num ) :
    n = len ( num )
    sumofdigit = [ ]
    sumofdigit.append ( ord ( num [ 0 ] ) - ord('0') )
    res = sumofdigit [ 0 ]
    for i in range ( 1 , n ) :
        numi = ord ( num [ i ] ) - ord ( '0' )
        sumofdigit.append ( ( i + 1 ) + numi + 10 + sumofdigit [ i - 1 ] )
        res += sumofdigit [ i ]
    return res

SUM_PAIRWISE_PRODUCTS | def findSum ( n ) :
    sm = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , n + 1 ) :
            sm = sm + i * j
    return sm

SUM_PAIRWISE_PRODUCTS_1 | def findSum ( n ) :
    multiTerms = n * ( n + 1 ) // 2
    sm = multiTerms
    for i in range ( 2 , n + 1 ) :
        multiTerms = multiTerms - ( i - 1 )
        sm = sm + multiTerms * i
    return sm

SUM_PAIRWISE_PRODUCTS_2 | def findSum ( n ) :
    return n * ( n + 1 ) * ( n + 2 ) * ( 3 * n + 1 ) / 24

SUM_SERIES_0_6_0_06_0_006_0_0006_N_TERMS | def sumOfSeries ( n ) :
    return ( ( 0.666 ) * ( 1 - 1 / pow ( 10 , n ) ) )

SUM_SERIES_12_32_52_2N_12 | def sumOfSeries ( n ) :
    sum = 0
    for i in range ( 1 , n + 1 ) :
        sum = sum + ( 2 * i - 1 ) * ( 2 * i - 1 )
    return sum

SUM_SERIES_23_45_67_89_UPTO_N_TERMS | def seriesSum ( n ) :
    i = 1
    res = 0.0
    sign = True
    while ( n > 0 ) :
        n = n - 1
        if ( sign ) :
            sign = False
            res = res + ( i + 1 ) / ( i + 2 )
            i = i + 2
        else :
            sign = True
            res = res - ( i + 1 ) / ( i + 2 )
            i = i + 2
    return res

SUM_SQUARES_BINOMIAL_COEFFICIENTS | def sumofsquare ( n ) :
    C = [ [ 0 for i in range ( n + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( 0 , n + 1 ) :
        for j in range ( 0 , min ( i , n ) + 1 ) :
            if ( j == 0 or j == i ) :
                C [ i ] [ j ] = 1
            else :
                C [ i ] [ j ] = ( C [ i - 1 ] [ j - 1 ] + C [ i - 1 ] [ j ] )
    sum = 0
    for i in range ( 0 , n + 1 ) :
        sum = sum + ( C [ n ] [ i ] * C [ n ] [ i ] )
    return sum

SUM_TWO_LARGE_NUMBERS | def findSum(str1, str2):
    if (len(str1) > len(str2)):
        t = str1
        str1 = str2
        str2 = t
    str = ""
    n1 = len(str1)
    n2 = len(str2)
    str1 = str1[:: - 1]
    str2 = str2[:: - 1]
    carry = 0
    for i in range(n1):
        sum = ((ord(str1[i]) - 48) + ((ord(str2[i]) - 48) + carry))
        if sum < 0:
            str += chr(sum % -10 + 48)
        else:
            str += chr(sum % 10 + 48)
        carry = int(sum / 10)
    for i in range(n1, n2):
        sum = ((ord(str2[i]) - 48) + carry)
        if sum < 0:
            str += chr(sum % -10 + 48)
        else:
            str += chr(sum % 10 + 48)
        carry = (int)(sum / 10)
    if (carry):
        str += chr(carry + 48)
    str = str[:: - 1]
    return str

SWAP_BITS_IN_A_GIVEN_NUMBER | def swapBits ( x , p1 , p2 , n ) :
    set1 = ( x >> p1 ) & ( ( 1 << n ) - 1 )
    set2 = ( x >> p2 ) & ( ( 1 << n ) - 1 )
    xor = ( set1 ^ set2 )
    xor = ( xor << p1 ) | ( xor << p2 )
    result = x ^ xor
    return result

SWAP_TWO_NIBBLES_BYTE | def swapNibbles ( x ) :
    return ( ( x & 0x0F ) << 4 | ( x & 0xF0 ) >> 4 )

SWAP_TWO_NUMBERS_WITHOUT_USING_TEMPORARY_VARIABLE | def swap ( xp , yp ) :
    xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
    yp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]
    xp [ 0 ] = xp [ 0 ] ^ yp [ 0 ]

TEMPLE_OFFERINGS | def offeringNumber ( n , templeHeight ) :
    sum = 0
    for i in range ( n ) :
        left = 0
        right = 0
        for j in range ( i - 1 , - 1 , - 1 ) :
            if ( templeHeight [ j ] < templeHeight [ j + 1 ] ) :
                left += 1
            else :
                break
        for j in range ( i + 1 , n ) :
            if ( templeHeight [ j ] < templeHeight [ j - 1 ] ) :
                right += 1
            else :
                break
        sum += max ( right , left ) + 1
    return sum

THIRD_LARGEST_ELEMENT_ARRAY_DISTINCT_ELEMENTS | def thirdLargest ( arr , arr_size ) :
    if ( arr_size < 3 ) :
        print ( " Invalid Input " )
        return
    first = arr [ 0 ]
    for i in range ( 1 , arr_size ) :
        if ( arr [ i ] > first ) :
            first = arr [ i ]
    second = - sys.maxsize
    for i in range ( 0 , arr_size ) :
        if ( arr [ i ] > second and arr [ i ] < first ) :
            second = arr [ i ]
    third = - sys.maxsize
    for i in range ( 0 , arr_size ) :
        if ( arr [ i ] > third and arr [ i ] < second ) :
            third = arr [ i ]
    print ( "The Third Largest" , "element is" , third )

THIRD_LARGEST_ELEMENT_ARRAY_DISTINCT_ELEMENTS_1 | def thirdLargest ( arr , arr_size ) :
    if ( arr_size < 3 ) :
        print ( " Invalid Input " )
        return
    first = arr [ 0 ]
    second = - sys.maxsize
    third = - sys.maxsize
    for i in range ( 1 , arr_size ) :
        if ( arr [ i ] > first ) :
            third = second
            second = first
            first = arr [ i ]
        elif ( arr [ i ] > second ) :
            third = second
            second = arr [ i ]
        elif ( arr [ i ] > third ) :
            third = arr [ i ]
    print ( "The third Largest" , "element is" , third )

TILING_WITH_DOMINOES | def countWays ( n ) :
    A = [ 0 ] * ( n + 1 )
    B = [ 0 ] * ( n + 1 )
    A [ 0 ] = 1
    A [ 1 ] = 0
    B [ 0 ] = 0
    B [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        A [ i ] = A [ i - 2 ] + 2 * B [ i - 1 ]
        B [ i ] = A [ i - 1 ] + B [ i - 2 ]
    return A [ n ]

TOTAL_NUMBER_OF_NON_DECREASING_NUMBERS_WITH_N_DIGITS_1 | def countNonDecreasing ( n ) :
    N = 10
    count = 1
    for i in range ( 1 , n + 1 ) :
        count = int ( count * ( N + i - 1 ) )
        count = int ( count / i )
    return count

TRIANGULAR_MATCHSTICK_NUMBER | def numberOfSticks ( x ) :
    return ( 3 * x * ( x + 1 ) ) / 2

TRIANGULAR_NUMBERS | def isTriangular ( num ) :
    if ( num < 0 ) :
        return False
    sum , n = 0 , 1
    while ( sum <= num ) :
        sum = sum + n
        if ( sum == num ) :
            return True
        n += 1
    return False

TURN_OFF_THE_RIGHTMOST_SET_BIT | def fun ( n ) :
    return n & ( n - 1 )

UNIQUE_CELLS_BINARY_MATRIX | def countUnique ( mat , n , m ) :
    rowsum = [ 0 ] * n
    colsum = [ 0 ] * m
    for i in range ( n ) :
        for j in range ( m ) :
            if ( mat [ i ] [ j ] != 0 ) :
                rowsum [ i ] += 1
                colsum [ j ] += 1
    uniquecount = 0
    for i in range ( n ) :
        for j in range ( m ) :
            if ( mat [ i ] [ j ] != 0 and rowsum [ i ] == 1 and colsum [ j ] == 1 ) :
                uniquecount += 1
    return uniquecount

WAYS_REMOVE_ONE_ELEMENT_BINARY_STRING_XOR_BECOMES_ZERO | def xorZero ( str ) :
    one_count = 0
    zero_count = 0
    n = len ( str )
    for i in range ( 0 , n , 1 ) :
        if ( str [ i ] == '1' ) :
            one_count += 1
        else :
            zero_count += 1
    if ( one_count % 2 == 0 ) :
        return zero_count
    return one_count

WAYS_TO_WRITE_N_AS_SUM_OF_TWO_OR_MORE_POSITIVE_INTEGERS | def CountWays ( n ) :
    table = [ 0 ] * ( n + 1 )
    table [ 0 ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i , n + 1 ) :
            table [ j ] += table [ j - i ]
    return table [ n ]

WAYS_TRANSFORMING_ONE_STRING_REMOVING_0_CHARACTERS | def countTransformation ( a , b ) :
    n = len ( a )
    m = len ( b )
    if m == 0 :
        return 1
    dp = [ [ 0 ] * ( n + 1 ) for _ in range ( m + 1 ) ]
    for i in range ( m ) :
        for j in range ( i , n ) :
            if i == 0 :
                if j == 0 :
                    if a [ j ] == b [ i ] :
                        dp [ i ] [ j ] = 1
                    else :
                        dp [ i ] [ j ] = 0
                elif a [ j ] == b [ i ] :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ] + 1
                else :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ]
            else :
                if a [ j ] == b [ i ] :
                    dp [ i ] [ j ] = ( dp [ i ] [ j - 1 ] + dp [ i - 1 ] [ j - 1 ] )
                else :
                    dp [ i ] [ j ] = dp [ i ] [ j - 1 ]
    return dp [ m - 1 ] [ n - 1 ]

WRITE_AN_EFFICIENT_METHOD_TO_CHECK_IF_A_NUMBER_IS_MULTIPLE_OF_3 | def isMultipleOf3 ( n ) :
    odd_count = 0
    even_count = 0
    if ( n < 0 ) :
        n = - n
    if ( n == 0 ) :
        return 1
    if ( n == 1 ) :
        return 0
    while ( n ) :
        if ( n & 1 ) :
            odd_count += 1
        if ( n & 2 ) :
            even_count += 1
        n = n >> 2
    return isMultipleOf3 ( abs ( odd_count - even_count ) )

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO | def isPowerOfTwo ( n ) :
    if ( n == 0 ) :
        return False
    while ( n != 1 ) :
        if ( n % 2 != 0 ) :
            return False
        n = n // 2
    return True

WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO_1 | def isPowerOfTwo ( x ) :
    return ( x and ( not ( x & ( x - 1 ) ) ) )

ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION | def nearestSmallerEqFib ( n ) :
    if ( n == 0 or n == 1 ) :
        return n
    f1 , f2 , f3 = 0 , 1 , 1
    while ( f3 <= n ) :
        f1 = f2 
        f2 = f3 
        f3 = f1 + f2 
    return f2 

