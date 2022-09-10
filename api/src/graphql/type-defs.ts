import { mergeTypeDefs } from "@graphql-tools/merge";

import { typeDefs as authTypes } from "@/graphql/auth";
import { typeDefs as cabinTypes } from "@/graphql/cabins";
import { typeDefs as permissionTypes } from "@/graphql/permissions";
import { typeDefs as scalarTypes } from "@/graphql/scalars";
import { typeDefs as userTypes } from "@/graphql/users";

export const typeDefs = mergeTypeDefs([userTypes, permissionTypes, cabinTypes, scalarTypes, authTypes]);

export default typeDefs;
