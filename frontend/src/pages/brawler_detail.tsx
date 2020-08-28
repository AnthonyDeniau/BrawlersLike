import React, { useState, useEffect } from "react";
import { Row, Col, Space, Layout, Typography, Button } from "antd";
import { ApolloClient, InMemoryCache, gql } from "@apollo/client";
import { BrawlerText, BrawlerTitle } from "../components/BrawlerText";

export interface BrawlerDetailPageProps {}

const client = new ApolloClient({
  uri: "/graphql/",
  cache: new InMemoryCache(),
});

const BrawlerDetailPage: React.SFC<BrawlerDetailPageProps> = () => {
  const [brawlerData, setbrawlerData] = useState<any>(null);

  useEffect(() => {
    client
      .query({
        query: gql`
          query GetBrawler {
            brawler(id: 3) {
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
        background:
          "radial-gradient(30.05% 140.89% at 50% 50%, #2AF5FF 0%, rgba(1, 71, 187, 0.92) 100%)",
      }}
    >
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
          <Button type="primary" style={{ marginTop: "50px" }}>
            Choisir
          </Button>
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
            style={{ height: "40%", width: "auto" }}
          />
        </Col>
        <Col span={8}>
          Stats
          {brawlerData?.data?.brawler.speed}
        </Col>
      </Row>
    </Layout>
  );
};

export default BrawlerDetailPage;
