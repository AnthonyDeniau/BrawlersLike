
import React, { FunctionComponent, useEffect, useState } from 'react'
import { ApolloClient, InMemoryCache, gql } from "@apollo/client";
import { Layout, List } from 'antd';
import { Link } from "react-router-dom";
import { BrawlerTitle } from "../components/BrawlerText";



const client = new ApolloClient({
  uri: "/graphql/",
  cache: new InMemoryCache(),
});

export const BrawlerListPage = () => {
    const [brawlerData, setbrawlerData] = useState<any>(null);

  useEffect(() => {
    client
      .query({
        query: gql`
          query GetBrawler {
            brawlers {
              id
              name
              avatar
            }
          }
        `,
      })
      .then((value) => setbrawlerData(value))
      .catch((error) => console.log(error));
  }, []);
    return (
      <Layout
      style={{
        padding: "25px",
        background: "linear-gradient(to right, #3F5EFB, #FC466B)"

      }}
    >
      <BrawlerTitle level={1}>BRAWLERS</BrawlerTitle>
      <br/>
      <List
        grid={{ gutter: 16, column: 3 }}
        dataSource={brawlerData?.data?.brawlers}
        renderItem={(brawler: any) => (
          <List.Item>
            <Link to={`/brawler/${brawler.id}`}>
            <BrawlerCard name={brawler.name} avatarUrl={brawler.avatar}/>
            </Link>
          </List.Item>
        )}
      />
    </Layout>)

}

type BrawlerCardProps = {
  name: string;
  avatarUrl: string;
}

const BrawlerCard: FunctionComponent<BrawlerCardProps> = ({name, avatarUrl }) => <div style={{
  borderRadius: "4px",
  boxShadow: "3px 6px 0px rgba(0, 0, 0, 0.25)",
  border: "1px solid black",
  borderBottom: "3px solid black",
  borderRight: "2px solid black",
  width: "203px",
}}>
  <img src={avatarUrl} />
  <span style={{
    position: "absolute",
    left: "27px",
    bottom: 0
  }}><BrawlerTitle level={3}>{name}</BrawlerTitle></span>
</div>
