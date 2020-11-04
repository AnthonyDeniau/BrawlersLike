import React, { useState, useEffect, FunctionComponent } from "react";
import { Row, Col, Space, Layout, Typography, Button } from "antd";
import { ApolloClient, InMemoryCache, gql } from "@apollo/client";
import { BrawlerText, BrawlerTitle } from "../components/BrawlerText";
import { Link, useHistory, useParams } from "react-router-dom";
import {
  YellowBrawlerButton,
  GrayBrawlerButton,
} from "../components/BrawlerButton";

export interface BrawlerDetailPageProps {}

const client = new ApolloClient({
  uri: "/graphql/",
  cache: new InMemoryCache(),
});

type BrawlerDetailPageParams = {
  brawlerId: string;
};

const BrawlerDetailPage: React.SFC<BrawlerDetailPageProps> = () => {
  const history = useHistory();
  const { brawlerId } = useParams<BrawlerDetailPageParams>();
  const [brawlerData, setbrawlerData] = useState<any>(null);

  useEffect(() => {
    client
      .query({
        query: gql`
          query GetBrawler {
            brawler(id: ${brawlerId}) {
              name
              description
              cost
              avatar
              speed
              health
            }
          }
        `,
      })
      .then((value) => setbrawlerData(value))
      .catch((error) => console.log(error));
  }, []);
  console.log(brawlerData);
  return (
    <Layout
      style={{
        background: "linear-gradient(to left, #0575e6, #021b79)",
      }}
    >
      <div
        style={{
          position: "absolute",
          left: "12px",
          top: "12px",
          zIndex: 1000,
        }}
      >
        <GrayBrawlerButton
          style={{ height: "30px", width: "70px", textAlign: "center" }}
          onClick={() => console.log("click BACK", history.push("/brawlers"))}
        >
          <BrawlerTitle level={4} style={{ cursor: "pointer" }}>
            BACK
          </BrawlerTitle>
        </GrayBrawlerButton>
      </div>

      <Row style={{ height: "100vh" }}>
        <Col
          span={8}
          style={{
            textAlign: "center",
            display: "flex",
            justifyContent: "center",
            flexDirection: "column",
            padding: "20px",
          }}
        >
          <BrawlerTitle>{brawlerData?.data?.brawler.name}</BrawlerTitle>
          <BrawlerTitle level={3}>Tireur d'élite</BrawlerTitle>
          <BrawlerText>{brawlerData?.data?.brawler.description}</BrawlerText>
          <YellowBrawlerButton style={{ marginTop: "15px" }}>
            <BrawlerTitle level={3}>Choisir</BrawlerTitle>
          </YellowBrawlerButton>
        </Col>
        <Col
          span={8}
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <img
            src={brawlerData?.data?.brawler.avatar}
            style={{ height: "60%", width: "auto" }}
          />
        </Col>
        <Col
          span={8}
          style={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <div
            style={{
              background: "#3B87E2",
              border: "1px solid #2B67BE",
              borderRadius: "4px",
              width: "25vw",
              height: "60%",
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <BrawlerStat
              backgroundColor="#143860"
              statBackgroundColor="#3B1010"
              textColor="#EB9B99"
              iconUrl="https://cdn.starlist.pro/icon/Damage.png"
              title="ATTACK"
            />
            <BrawlerStat
              backgroundColor="#143860"
              statBackgroundColor="#193B10"
              textColor="#B0FBA2"
              iconUrl="https://cdn.starlist.pro/icon/Health.png"
              title="HEALTH"
            />
            <BrawlerStat
              backgroundColor="#143860"
              statBackgroundColor="#0B2757"
              textColor="#80C9FA"
              iconUrl="https://cdn.starlist.pro/icon/Info.png"
              title="SUPP"
            />
          </div>
        </Col>
      </Row>
    </Layout>
  );
};

export default BrawlerDetailPage;

type BrawlerStatProps = {
  backgroundColor: string;
  statBackgroundColor: string;
  textColor: string;
  iconUrl: string;
  title: string;
};
const BrawlerStat: FunctionComponent<BrawlerStatProps> = ({
  backgroundColor,
  statBackgroundColor,
  textColor,
  iconUrl,
  title,
}) => (
  <div
    style={{
      background: backgroundColor,
      height: "32px",
      width: "90%",
      marginBottom: "30px",
      position: "relative",
    }}
  >
    <div
      style={{
        position: "absolute",
        top: "4px",
        right: "8px",
        background: statBackgroundColor,
        border: "2px solid #000000",
        width: "60%",
        height: "24px",
        transform: "skewX(-10deg)",
      }}
    ></div>
    <div style={{ position: "absolute", top: "-33px", left: "60px" }}>
      <BrawlerTitle level={3} style={{ color: textColor }}>
        {title}
      </BrawlerTitle>
    </div>
    <img src={iconUrl} style={{ height: "50px", marginTop: "-15px" }} />
  </div>
);
