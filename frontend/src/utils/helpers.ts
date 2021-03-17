import { ContactInfo } from "@interfaces/cabins";
import validator from "validator";

export const generateQueryString = (values: Record<string, any>): string => {
  const valueList: string[] = [];

  Object.keys(values).forEach((name) => {
    if (values[name]) {
      const value = values[name];
      valueList.push(`${name}=${value}`);
    }
  });
  return "?" + valueList.join("&");
};

export const allValuesDefined = (obj: Record<string, any>): boolean => {
  let empty = true;
  Object.values(obj).forEach((val) => {
    if (val === undefined && val != 0) {
      empty = false;
    }
  });
  return empty;
};

export const range = (start: number, end: number): number[] => {
  const res: number[] = [];
  for (let i = start; i <= end; i++) {
    res.push(i);
  }
  return res;
};

export const validateName = (name: string) => name.length > 0;

export const validateEmail = (email: string): boolean => validator.isEmail(email);

export const validateSelect = (numberIndok: number, numberExternal: number): boolean =>
  numberIndok > 0 || numberExternal > 0;

export const validatePhone = (phone: string): boolean => (phone ? validator.isMobilePhone(phone) : false);

export const validateInputForm = (inputValues: Record<string, any>) => {
  const selectValidity = validateSelect(inputValues.numberIndok, inputValues.numberExternal);

  const updatedValidations = {
    firstName: validateName(inputValues.firstName),
    lastName: validateName(inputValues.lastName),
    email: validateEmail(inputValues.email),
    phone: validatePhone(inputValues.phone),
    numberIndok: selectValidity,
    numberExternal: selectValidity,
    triggerError: false,
  };

  return updatedValidations;
};

export const isFormValid = (inputValues: ContactInfo) => {
  const validations = validateInputForm(inputValues);
  const { triggerError, ...evaluated } = validations;

  return Object.values(evaluated).every((val) => val);
};
