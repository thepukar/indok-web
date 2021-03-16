import { gql } from "@apollo/client";

export const LISTINGS = gql`
  query {
    listings {
      id
      title
      description
      startDatetime
      deadline
      endDatetime
      url
      slug
      organization {
        name
        color
      }
    }
  }
`;

export const LISTING = gql`
  query listing($ID: ID!) {
    listing(id: $ID) {
      id
      title
      description
      startDatetime
      deadline
      endDatetime
      url
      organization {
        name
        description
        color
      }
      survey {
        id
      }
    }
  }
`;

export const LISTING_WITH_RESPONDERS = gql`
  query listing($ID: ID!) {
    listing(id: $ID) {
      id
      title
      description
      startDatetime
      deadline
      endDatetime
      url
      survey {
        id
        responders {
          id
          firstName
          lastName
        }
      }
    }
  }
`;
