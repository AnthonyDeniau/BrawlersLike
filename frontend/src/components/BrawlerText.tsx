import React, { FunctionComponent } from "react";
import "./BrawlerText.css";

export const BrawlerText: FunctionComponent = ({ children }) => {
  return <span className="brawler-text">{children}</span>;
};

type BrawlerTitleType = {
  level?: 5 | 1 | 2 | 3 | 4 | undefined;
};
export const BrawlerTitle: FunctionComponent<BrawlerTitleType> = ({
  level,
  children,
}) => {
  const titleLevel = level ? level : 1;
  return (
    <span className={"brawler-title-" + titleLevel?.toString()}>
      {children}
    </span>
  );
};
