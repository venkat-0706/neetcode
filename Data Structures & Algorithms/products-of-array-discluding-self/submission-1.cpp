class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
     int product = 1;
    int zero_count = 0;
    for (const int &num : nums) {
    if (num == 0) {
      zero_count++;
    } else {
      product *= num;
    }
  }

  std::vector<int> result(nums.size());

  std::transform(nums.begin(), nums.end(), result.begin(), [&](int num) {
    if (zero_count > 1)
      return 0;
    if (zero_count == 1)
      return (num == 0) ? product : 0; // only the zero gets the product others get clapped
    return product / num;
  });

  return result;
}
   };