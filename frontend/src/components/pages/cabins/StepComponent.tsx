import { Typography } from "@mui/material";
import React from "react";

import { ContactInfo, ContactInfoValidations, DatePick } from "@/interfaces/cabins";
import { Cabin } from "@/types/cabins";

import CabinContactInfo from "./CabinContactInfo";
import CheckInOut from "./CheckInOut";
import ExtraInfoSite from "./ExtraInfoSite";
import PaymentSite from "./PaymentSite";
import ReceiptSite from "./ReceiptSite";

type Props = {
  activeStep: number;
  allCabins: Cabin[];
  chosenCabins: Cabin[];
  contactInfo: ContactInfo;
  datePick: DatePick;
  validations?: ContactInfoValidations;
  errorTrigger: boolean;
  setContactInfo: React.Dispatch<React.SetStateAction<ContactInfo>>;
  setChosenCabins: React.Dispatch<React.SetStateAction<Cabin[]>>;
  setDatePick: React.Dispatch<React.SetStateAction<DatePick>>;
  setExtraInfo: React.Dispatch<React.SetStateAction<string>>;
};

const StepComponent: React.FC<Props> = (props) => {
  switch (props.activeStep) {
    case 0:
      // Choose cabin
      return (
        <CheckInOut
          allCabins={props.allCabins}
          chosenCabins={props.chosenCabins}
          setChosenCabins={props.setChosenCabins}
          setDatePick={props.setDatePick}
        />
      );
    case 1:
      // Choose contact info
      return (
        <CabinContactInfo
          contactInfo={props.contactInfo}
          setContactInfo={props.setContactInfo}
          validations={props.validations}
          errorTrigger={props.errorTrigger}
          chosenCabins={props.chosenCabins}
        />
      );
    case 2:
      // Extra info site
      return (
        <ExtraInfoSite setExtraInfo={props.setExtraInfo} chosenCabins={props.chosenCabins} datePick={props.datePick} />
      );
    case 3:
      // Payment
      return (
        <PaymentSite chosenCabins={props.chosenCabins} datePick={props.datePick} contactInfo={props.contactInfo} />
      );
    case 4:
      // Receipt
      return (
        <ReceiptSite
          chosenCabins={props.chosenCabins}
          datePick={props.datePick}
          contactInfo={props.contactInfo}
          mailSent
        />
      );

    default:
      return <Typography>Step not found</Typography>;
  }
};

export default StepComponent;
