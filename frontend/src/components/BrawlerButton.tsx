import React, { FunctionComponent } from "react";

export const YellowBrawlerButton: FunctionComponent<React.HTMLProps<
  HTMLDivElement
>> = ({ children, ...otherProps }) => {
  return (
    <div
      {...otherProps}
      style={{
        ...otherProps.style,
        cursor: "pointer",
        transform: "skewX(-10deg)",
        background: "#E7C443",
        border: "1px solid #000000",
        boxSizing: "border-box",
        boxShadow:
          "0px 2px 0px rgba(0, 0, 0, 0.4), inset 1px -4px 0px rgba(123, 49, 8, 0.25), inset -1px 4px 0px rgba(255, 245, 151, 0.54)",
        borderRadius: "3px",
      }}
    >
      {children}
    </div>
  );
};

export const GrayBrawlerButton: FunctionComponent<React.HTMLProps<
  HTMLDivElement
>> = ({ children, ...otherProps }) => {
  return (
    <div
      {...otherProps}
      style={{
        ...otherProps.style,
        cursor: "pointer",
        transform: "skewX(-10deg)",
        background: "#353C4E",
        border: "1px solid #000000",
        boxSizing: "border-box",
        boxShadow:
          "0px 2px 0px rgba(0, 0, 0, 0.4), inset 1px -4px 0px rgba(0, 0, 0, 0.42), inset -1px 4px 0px rgba(255, 255, 255, 0.26)",
        borderRadius: "3px",
      }}
    >
      {children}
    </div>
  );
};
