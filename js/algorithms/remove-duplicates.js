export const removeDuplicates = (arr) => {
  const newArr = [...new Set(arr)];
  return newArr;
};
