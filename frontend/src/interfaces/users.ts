import { Organization } from "./organizations";

export interface User {
  id: string;
  username: string;
  isStaff: boolean;
  isActive: boolean;
  isSuperuser: boolean;
  email: string;
  firstName: string;
  lastName: string;
  feideUserid: string;
  lastLogin: string;
  dateJoined: string;
  year: number;
  phone: string;
  events?: { id: string }[];
  organizations?: Organization[];
}
