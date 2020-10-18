import { gql } from "@apollo/client";

export const CREATE_LISTING = gql`
    mutation createListing(
        $title: String!
        $description: String!
        $startDateTime: DateTime!
        $deadline: DateTime!
        $endDateTime: DateTime!
        $url: String!
        $organizationId: ID
    ) {
        createListing(
            listingData: {
                title: $title
                description: $description
                startDateTime: $startDateTime
                deadline: $deadline
                endDateTime: $endDateTime
                url: $url
                organizationId: $organizationId
            }
        ) {
            listing {
                id
                title
                description
                startDateTime
                deadline
                endDateTime
                url
                organization {
                    id
                    name
                }
            }
            ok
        }
    }
`;

export const DELETE_LISTING = gql`
    mutation deleteListing($ID: ID!) {
        deleteListing(id: $ID) {
            ok
            listingId
        }
    }
`;

export const CREATE_RESPONSE = gql`
    mutation createResponse($response: String!, $applicantId: ID!, $listingId: ID!) {
        createResponse(responseData: { response: $response, applicantId: $applicantId, listingId: $listingId }) {
            response {
                id
                response
            }
            ok
        }
    }
`;

export const DELETE_RESPONSE = gql`
    mutation deleteResponse($ID: ID!) {
        deleteResponse(responseId: $ID) {
            response {
                id
            }
            ok
        }
    }
`;

export const CREATE_ORGANIZATION = gql`
    mutation createOrganization($name: String!, $description: String!) {
        createOrganization(organizationData: { name: $name, description: $description }) {
            organization {
                id
                name
                description
                slug
            }
        }
    }
`;
