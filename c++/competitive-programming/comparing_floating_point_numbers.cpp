/*
 * It is risky to compare floating point numbers with the == operator, because it
 * is possible that the values should be equal, but they are not, because of precision
 * errors. A better way to compare floating point numbers is to assume that two
 * numbers are equal if the difference between them is less than epsilon, where epsilon is a 
 * small number.
 *
 * In practice, the numbers can be compared as follows (epsilon = 10^-9)
 */

if (abs(a - b) < 1e-9) {
  // a and b are equal
}

